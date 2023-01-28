<script>
    export let defaultDisplay = true;
</script>

{#if defaultDisplay}
    <header>
        <h1>My App</h1>
        <a href="/">Menu</a>
        <a href="/dishes">Dishes</a>
        <a href="/about">About</a>
    </header>
{:else}
    <slot></slot>
{/if}

<style>
    header {
        height: 100px;
        width: 100%;
        background-color: var(--secondary-color);
        display: flex;
        justify-content: center;
        align-items: center;
        margin-bottom: 20px;
    }
</style>