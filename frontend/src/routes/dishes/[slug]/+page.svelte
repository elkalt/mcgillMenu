<script lang="typescript">  
    import StarRating from "@ernane/svelte-star-rating";
    import { onMount } from 'svelte';
    import { page } from '$app/stores';
    
    export let data;

    function areNotes() {
        let numDietNotes = false;
        Object.keys(data.response_json.data).forEach(( key ) => {
            if (data.response_json.data[key] && key !== 'ratings') {
                numDietNotes = true;
            }
        });
        return numDietNotes;
    }

    let averageRating = 0;
    let totalRatings = 0;
    const keyConverter = {
        gf: "gluten free",
        v: "vegetarian",
        ve: "vegan",
        df: "dairy free",
        msc: "marine stewardship council",
        h: "halal"
    };

    onMount(() => {
        if (data.response_json.data.ratings !== undefined) {
            data.response_json.data.ratings.forEach(( element ) => {
                totalRatings++;
                averageRating += element.rating;
            });
            averageRating = averageRating / totalRatings;
        }
    });

    function getRating(ratings) {
        let rating = 0;
        let count = 0;
        // @ts-ignore
        for (let i = 0; i < ratings.length; i++) {
        // @ts-ignore
            rating += ratings[i].rating;
            count++;
        }
        if (Number.isNaN(rating / count)) {
            return 0;
        }
        return rating / count;
    }

    let config = (rating) => {
        return {
                    score:rating,
                    readOnly: false,
                    countStars: 5,
                    range: {
                        min: 0, 
                        max: 5, 
                        step: 1
                    },
                    // showScore: true,
                    starConfig: {
                        size: 30,
                        fillColor: "#ffbc2d",
                        strokeColor: "#BB8511",
                        unfilledColor: '#FFF',ledColor: '#000'
                    }
                }} 




        const post_url = (rating) => {
            return `http://louismeunier.pythonanywhere.com/api/dishes/${$page.params.slug}/rate?rating=${rating}&dining_hall`
        }
</script>
  

<div class="container_local">
    <div class="item_title">
        <h1>{ $page.params.slug }</h1>
    </div>
    <div class="item_tall">
        <h2>Rating:</h2>
            <StarRating 
            on:change={(e => {
                console.log(e.target.value);
                fetch(post_url(e.target.value),
                    {
                        method: 'POST',
                        headers: {
                            'Content-Type': 'application/json'
                        },
                    }
                ).then(async (response) => {
                    if (response.ok) {
                        console.log(response)
                        // reload website
                        const body = await response.json();
                        // @ts-ignore
                        data.response_json.data["ratings"] = body;
                        // config = config(getRating(response))
                        console.log("success");
                    } else {
                        console.log("failure");
                    }
                });
            })}
                config={config(getRating(data.response_json.data["ratings"]))}
                />
    </div>

    <div class="item_tall">
        <h2>Dietary notes:</h2>
        {#each Object.keys(data.response_json.data) as note}
            {#if data.response_json.data[note] && note !== 'ratings'}
                <div class="pill_list {note}" title={keyConverter[note]}>{note.toUpperCase()}</div>
            {/if}
        {/each}
        {#if areNotes() == false}
            <p>No dietary notes</p>
        {/if}
    </div>
</div>

<style>
    .pill_list {
        display: inline-block;
        padding: 0.5em;
        margin: 0.5em;
        border-radius: 0.5em;
        font-weight: 700;
        font-size: 1.1rem;
    }
    .container_local {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        grid-template-rows: repeat(3, 1fr);
        justify-items: center;
    }
    .item_title {
        grid-column: 1 / 3;
        grid-row: 1 / 2;
    }
    .item_tall {
        grid-row: 2 / 4;
        text-align: center;
    }
</style>