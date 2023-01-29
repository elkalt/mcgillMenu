<script>
    export let defaultDisplay = true;
</script>

<header>
    <div class="title">
        <h1>Campus</h1> 
        <img src="bird.png" height="60px"/>
        
        <h1>Critics</h1>
    </div>
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
        font-size: 2.8em;
    }
    header {
        height: 100px;
        width: 100%;
        text-align: center;
        padding-bottom: 20px;
        border-bottom: 2px solid var(--dark-pink);
    }

    .title {
        display: flex;
        flex-direction: row;
        width: 100%;
        justify-content: center;
        align-items: center;
    }
</style>