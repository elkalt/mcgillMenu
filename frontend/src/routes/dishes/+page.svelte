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
    {#each Object.keys(data.data) as dish}
        {#if data.data[dish].name != undefined}
            <li>
                <a href={`/dishes/${data.data[dish].name}`}> {data.data[dish].name} </a>
            </li>
        {/if}
    {/each}
</ul>