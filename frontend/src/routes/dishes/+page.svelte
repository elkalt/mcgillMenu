<script>
    // @ts-ignore
    import Header from "$lib/components/Header.svelte";
    /**
     * @type {any}
     */
     export let data;
</script>

<Header defaultDisplay={ false }>
    <a href="/">Menu</a> |
    <a href="/dishes" class="active">Dishes</a> |
    <a href="/about">About</a>
</Header>

<h1>All dishes</h1>

<ul>
    {#each data as dish}
        {#if dish.title != undefined}
            <li>
                {dish.name}
            </li>
        {/if}
    {/each}
</ul>