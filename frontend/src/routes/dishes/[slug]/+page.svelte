<script lang="typescript">  
    import StarRating from 'svelte-star-rating'
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
</script>
  
<h1>{ $page.params.slug }</h1>

<h2>Rating:</h2>
{#if data.response_json.data["ratings"].length > 0}
    <StarRating rating={getRating(data.response_json.data["ratings"])} 
        style="margin-bottom: 0;" config={{ "fullColor": "#ffbc2d" }} />
{:else}
    <p>Not rated yet</p>
{/if}

<h2>Dietary notes:</h2>
<ul>
    {#each Object.keys(data.response_json.data) as note}
        {#if data.response_json.data[note] && note !== 'ratings'}
            <div class="pill {note}" title={keyConverter[note]}>{note.toUpperCase()}</div>
        {/if}
    {/each}
    {#if areNotes() == false}
        <p>No dietary notes</p>
    {/if}
</ul>