<script>
    import Header from "../lib/components/Header.svelte";

    export let data;
</script>

<Header defaultDisplay={ false }>
    <a href="/" class="active">Menu</a> |
    <a href="/dishes">Dishes</a> |
    <a href="/about">About</a>
</Header>

<h1>home</h1>

<div class="container">
    {#each dining_day in data}
    <div class="item">{ data }</div>
</div>


<style>
    .container {
        display: grid;
        grid-template-columns: repeat(8, 1fr);
        grid-template-rows: repeat(5, 1fr);
    }
    .item {
        border: 1px solid black;
    }
</style>