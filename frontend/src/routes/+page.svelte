<script lang='ts'>
    import Header from "../lib/components/Header.svelte";
    import "/src/app.css";

    export let data;
    data = data.data;
    
    const daysOfWeek = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"];
    console.log(data.data);

</script>

<Header defaultDisplay={ false }>
    <a href="/" class="active">Menu</a> |
    <a href="/dishes">Dishes</a> |
    <a href="/about">About</a>
</Header>

<h2>This weeks menu:</h2>

<div class="container">
    <div></div>
    {#each daysOfWeek as day}
        <div class="item grid_header"><span style="text-transform: capitalize">{day}</span></div>
    {/each}
    <div class="item grid_header">Royal Victoria College</div>
    <div class="item grid_header" style="grid-column: 3/4">Douglas Hall</div>
    <div class="item grid_header" style="grid-column: 4/5">Bishop Mountain Hall</div>
    <div class="item grid_header" style="grid-column: 5/6">Carrefour Sherbrooke</div>
    <div class="item grid_header" style="grid-column: 6/7">New Residence Hall</div>
    {#each Object.keys(data) as id}
        {#each daysOfWeek as day}
            {#if data[id].menu[day] > 0}
                <div class="item">
                    <!-- <a href={``}>{ data.data[dining_day].menu[meal] }</a> -->
                </div>
            {:else}
                <div class="item">No menu available</div>
            {/if}
        {/each}
    {/each}
</div>


<style>
    .container {
        display: grid;
        grid-auto-columns: minmax(6, 1fr);
        grid-template-rows: repeat(8, 1fr);
        grid-gap: 1px;
        padding-left: 2rem;
        padding-right: 2rem;
        background-color: var(--background-color);
        grid-auto-flow: column;
    }
    .item {
        font-family: 'Montserrat', sans-serif;
        border: 1px solid var(--dark-pink);
        padding: 1rem;
        background-color: var(--background-color-accent);
        border-radius: 5px;
        text-align: center;
        justify-content: center;
        color: var(--secondary-color-accent2)
    }
    .grid_header {
        background-color: var(--background-color-accent2);
        color: var(--secondary-color);
        font-weight: 600;
    }
</style>