<script lang='ts'>
    import Header from "../lib/components/Header.svelte";
    import "/src/app.css";

    export let data;
</script>

<Header defaultDisplay={ false }>
    <a href="/" class="active">Menu</a> |
    <a href="/dishes">Dishes</a> |
    <a href="/about">About</a>
</Header>

<h2>This weeks menu:</h2>

<div class="container">
    <div class="item grid_header">Monday</div>
    <div class="item grid_header">Tuesday</div>
    <div class="item grid_header">Wednesday</div>
    <div class="item grid_header">Thursday</div>
    <div class="item grid_header">Friday</div>
    <div class="item grid_header">Saturday</div>
    <div class="item grid_header">Sunday</div>
    {#each Object.keys(data.data) as dining_day}
        {#if data.data[dining_day].menu.length > 0}
            {#each Object.keys(data.data[dining_day].menu) as meal}
                <div class="item">{ data.data[dining_day].menu[meal] }</div>
            {/each}
        {:else}
            <div class="item">No menu available</div>
            <div class="item">No menu available</div>
            <div class="item">No menu available</div>
            <div class="item">No menu available</div>
            <div class="item">No menu available</div>
            <div class="item">No menu available</div>
            <div class="item">No menu available</div>
        {/if}
    {/each}
</div>


<style>
    .container {
        display: grid;
        grid-template-columns: repeat(7, 1fr);
        grid-template-rows: repeat(6, 1fr);
        grid-gap: 1px;
        padding-left: 2rem;
        padding-right: 2rem;
        background-color: var(--background-color);
    }
    .item {
        font-family: 'Montserrat', sans-serif;
        border: 1px solid var(--dark-pink);
        padding: 1rem;
        background-color: var(--background-color-accent);
        border-radius: 5px;
        text-align: center;
        color: var(--secondary-color-accent2)
    }
    .grid_header {
        background-color: var(--background-color-accent2);
        color: var(--secondary-color);
        font-weight: 600;
    }
</style>