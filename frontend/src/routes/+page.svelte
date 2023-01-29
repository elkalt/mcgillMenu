<script lang='ts'>
    // @ts-nocheck
    import Header from "../lib/components/Header.svelte";
    import "/src/app.css";

    export let data;
    data = data.data;
    
    const allDaysOfWeek = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"];

    let visible = {
        "bmh": true,
        "cs": true,
        "dh": true,
        "nrh": true,
        "rvc": true
    }
</script>

<Header defaultDisplay={ false }>
    <a href="/" class="active">Menu</a> |
    <a href="/dishes">Dishes</a> |
    <a href="/about">About</a>
</Header>

<h1 style="text-align: center">This Weeks Menu</h1>

<div class="container">
    <div></div>

    {#each Object.keys(data) as id}
        <!-- Hall header -->
            <div class="item grid_header"
            style={visible[id] ? "padding:0;": ""}
            ><h3>
                <a href="#"
                    on:click = {() => {
                        visible[id] = !visible[id];
                    }}
                >{ !visible[id] ? data[id]["name"]  + " -" : `${id} +`}</a>
            </h3></div>
    {/each}

    {#each allDaysOfWeek as day}
    <!-- Day header -->
        <div class="item grid_header"><span style="text-transform: capitalize;"><h2>{day}</h2></span></div>
        
        {#each Object.keys(data) as id}
        <!-- Check if that day has a menu and if so, show it -->
        {#if !visible[id]}
            {#if data[id]["menu"][day] != undefined && Object.keys(data[id]["menu"][day]).length > 0}
                <div class="item">
                        {#each Object.keys(data[id]["menu"][day]) as meal}
                            <h2>{ meal }:</h2>
                            {#each Object.keys(data[id]["menu"][day][meal]) as dish}  
                                <li>
                                    <a href={`/dishes/${dish.replace("w/", "with ").replace("/", " or ")}`}>
                                        {dish.replace("w/", "with ").replace("/", " or ")} 
                                        <div style="display:flex;flex-direction:row; align-items:center;justify-content:center; gap: 0.5em;">
                                            {#each Object.keys(data[id]["menu"][day][meal][dish]) as diet}
                                                {#if data[id]["menu"][day][meal][dish][diet] === true}
                                                    <p style="color: var(--secondary-color-accent); font-weight: 400;  margin-bottom:0; margin-top:0.4em;">{diet.toUpperCase()}</p>
                                                {/if}
                                            {/each}
                                        </div>
                                    </a>
                                </li>
                            {/each}
                        {/each}
                    </div>
                {:else}
                    <div class="item">No menu available</div>
                {/if}
            {:else}
                <div class="item" style="font-weight:800; color:var(--secondary-color-accent2)"><bold>_</bold></div>
            {/if}
        {/each}
    {/each}
</div>


<style>
    .container {
        display: grid;
        grid-template-columns: repeat(8, auto);
        grid-template-rows: auto repeat(5, auto);
        grid-gap: 1px;
        background-color: var(--background-color);
        grid-auto-flow: column dense;
        margin: 1em;
    }
    .item {
        font-family: 'Montserrat', sans-serif;
        border: 1px solid var(--dark-pink);
        padding: 1rem;
        background-color: var(--background-color-accent);
        border-radius: 5px;
        text-align: center;
        justify-content: center;
        color: var(--secondary-color-accent2);
    }
    .grid_header {
        background-color: var(--background-color-accent2);
        color: var(--secondary-color);
        font-weight: 600;
    }
</style>