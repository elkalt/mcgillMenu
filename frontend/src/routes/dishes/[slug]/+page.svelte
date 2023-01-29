<script lang="typescript">  
    import StarRating from 'svelte-star-rating'
    import { onMount } from 'svelte'; 
    
    export let data;

    let averageRating = 0;
    let totalRatings = 0;
    onMount(() => {
        if (data.response_json.data.ratings !== undefined) {
            data.response_json.data.ratings.forEach(( element ) => {
                totalRatings++;
                averageRating += element.rating;
            });
            averageRating = averageRating / totalRatings;
        }
    });
</script>
  
<h1>{ data.response_json.data.name }</h1>

<h2>Rating:</h2>
{#if data.response_json.data.ratings == undefined}
    <StarRating rating={ averageRating } /> ({ totalRatings } ratings)
{:else}
    <p>Not rated yet</p>
{/if}

<h2>Dietary notes:</h2>
<ul>
    {#each data.response_json.data.options as note}
        <li>{ note }</li>
    {/each}
</ul>