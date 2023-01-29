<script>
    // @ts-ignore
    import Header from "$lib/components/Header.svelte";
    /**
     * @type {any}
     */
     export let data;
     console.log(data)
</script>

<Header defaultDisplay={ false }>
    <a href="/">Menu</a> |
    <a href="/dishes" class="active">Dishes</a> |
    <a href="/about">About</a>
</Header>

<h1>All dishes</h1>

<ul>
    {#each Object.keys(data.data) as dish}
        {#if dish != "_"}
            <li>
                <a href={`/dishes/${dish}`}> {dish} </a>
            </li>
        {/if}
    {/each}
</ul>