<script lang="ts">
  import type { IMenuItem } from "../../types";

  import AppMenuBar from "./AppMenuBar.svelte";
  import AppMenuIcon from "./AppMenuIcon.svelte";

  export let menuItems: IMenuItem[] = [];

  let menuCollapsed = true;

  function handleEvent(event) {
    menuCollapsed = !menuCollapsed;
  }
</script>

{#if menuCollapsed}
  <AppMenuIcon on:menuToggle={handleEvent} />
{:else}
  <AppMenuBar {menuItems} on:menuToggle={handleEvent} />
{/if}
