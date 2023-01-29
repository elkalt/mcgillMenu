<script>
    export let defaultDisplay = true;
</script>

<header>
    <h1>Better McGill Menu</h1>
    <nav>
        {#if defaultDisplay}
            <a href="/">Menu</a> |
            <a href="/dishes">Dishes</a> |
            <a href="/about">About</a>
        {:else}
            <slot></slot>
        {/if}
    </nav>
</header>

<style>
    header > h1 {
        color: var(--dark-pink);
    }
    header {
        height: 100px;
        width: 100%;
        text-align: center;
        padding-bottom: 5px;
        border-bottom: 2px solid var(--dark-pink);
    }
</style>