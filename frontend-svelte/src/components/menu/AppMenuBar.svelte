<script lang="ts">
  import { createEventDispatcher } from "svelte";
  import { fly, fade } from "svelte/transition";
  import type { IMenuItem } from "../../types";
  import UserAvatar from "../UserAvatar.svelte";
  import AppMenuItem from "./AppMenuItem.svelte";

  export let menuItems: IMenuItem[] = [];

  const dispatch = createEventDispatcher();

  function handleClick() {
    dispatch("menuToggle");
  }
</script>

<div
  on:click={handleClick}
  in:fly={{ x: -200, duration: 250, delay: 250 }}
  out:fly={{ x: -200, duration: 250 }}
>
  <UserAvatar />
  <ul>
    {#each menuItems as menuItem}
      <AppMenuItem {menuItem} />
    {/each}
  </ul>
</div>
<div class="overlay" on:click={handleClick} in:fade out:fade />

<style>
  div {
    position: fixed;
    z-index: 1;
    top: 0;
    left: 0;
    height: 100%;
    width: clamp(200px, 250px, 33%);
    background-color: var(--pal-secondary);
  }
  div.overlay {
    position: fixed;
    z-index: 0;
    top: 0;
    left: 0;
    height: 100%;
    width: 100%;
    background-color: #33333377;
  }
  ul {
    list-style: none;
    margin: var(--spacing);
    padding-left: 0px;
    padding-right: 0px;
  }
</style>
