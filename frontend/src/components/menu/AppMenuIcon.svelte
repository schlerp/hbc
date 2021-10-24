<script lang="ts">
  import { createEventDispatcher } from "svelte";
  import { fly } from "svelte/transition";

  const dispatch = createEventDispatcher();

  function handleClick() {
    dispatch("menuToggle");
  }
</script>

<div
  class="app-menu-wrapper"
  on:click={handleClick}
  in:fly={{ x: -100, duration: 250, delay: 250 }}
  out:fly={{ x: -100, duration: 250 }}
>
  <svg class="app-menu-icon" viewBox="0 0 50 40" width="30" height="30">
    <rect class="icon-element" width="50" height="10" />
    <rect class="icon-element" y="15" width="50" height="10" />
    <rect class="icon-element" y="30" width="50" height="10" />
  </svg>
</div>

<style>
  .app-menu-wrapper {
    background-color: var(--pal-secondary);
    height: calc(var(--spacing) * 10);
    width: calc(var(--spacing) * 10);
    border-radius: 50%;
    display: flex;
    align-items: center;
    justify-items: center;
    position: fixed;
    top: var(--spacing);
    left: var(--spacing);
    box-shadow: 2px 2px 3px 0px var(--pal-text-soft),
      3px 3px 5px 0px var(--pal-text-soft);
  }
  svg {
    display: block;
    margin: auto;
  }
  .icon-element {
    fill: var(--pal-text-dark);
  }
</style>
