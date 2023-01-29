<script lang="ts">
    // @ts-ignore
    import Header from "$lib/components/Header.svelte";
    import StarRating from "svelte-star-rating";
    /**
    * @type {any}
    */
    // @ts-ignore
    export let data;
    const keyConverter = {
        gf: "gluten free",
        v: "vegetarian",
        ve: "vegan",
        df: "dairy free",
        msc: "marine stewardship council",
        h: "halal"
    };
    
    // @ts-ignore
    function getRating(dish) {
        let rating = 0;
        let count = 0;
        // @ts-ignore
        for (let i = 0; i < data.data[dish].ratings.length; i++) {
        // @ts-ignore
            rating += data.data[dish].ratings[i].rating;
            count++;
        }
        if (Number.isNaN(rating / count)) {
            return 0;
        }
        return rating / count;
    }

    let sort = {
        "by": "rating",
        "order": "desc"
    }
    let name_prev = "ascending";
    let rating_prev = "ascending";
</script>

<Header defaultDisplay={ false }>
    <a href="/">Menu</a> |
    <a href="/dishes" class="active">Dishes</a> |
    <a href="/about">About</a>
</Header>

<h1 style="text-align: center">All dishes</h1>
<div class="filter_wrapper">
    <button on:click ={
        () => {
            sort.by = "name";
            if (sort.order == "asc") {
                sort.order = "desc";
                name_prev = "ascending";
            } else {
                sort.order = "asc";
                name_prev = "descending";
            }
        }
    }>
        name ({ name_prev })
    </button>
    <button on:click ={
        () => {
            sort.by = "rating";
            if (sort.order == "asc") {
                sort.order = "desc";
                rating_prev = "descending";
            } else {
                sort.order = "asc";
                rating_prev = "ascending";
            }
        }
    }>
        rating ({ rating_prev })
    </button>
</div>

<ul>
    {#each Object.keys(data.data).sort(
        (a, b) => {
            if (sort.by == "name") {
                if (sort.order == "asc") {
                    return a.localeCompare(b);
                } else {
                    return b.localeCompare(a);
                }
            } else {
                if (sort.order == "asc") {
                    return getRating(a) - getRating(b);
                } else {
                    return getRating(b) - getRating(a);
                }
            }
        }
    ) as dish}
        {#if dish != "_"}
            <li>
                <div style="flex: 1;">
                    <a href={`/dishes/${dish}`}> {dish} </a>
                    <div class="dietary">
                        {#each Object.keys(data.data[dish]) as key}
                            {#if data.data[dish][key] && key != "ratings"}
                                <div class="pill {key}" title={keyConverter[key]}>{key.toUpperCase()}</div>
                            {/if}
                        {/each}
                    </div>
                </div>
                <StarRating rating={getRating(dish)} 
                    style="margin-bottom: 0;" config={{ "fullColor": "#ffbc2d" }} />
            </li>
        {/if}
    {/each}
</ul>