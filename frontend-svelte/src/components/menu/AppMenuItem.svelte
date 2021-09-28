<script lang="ts">
  import { debug } from "svelte/internal";

  import { isUserAuthed } from "../../services/auth";
  import type { IMenuItem } from "../../types";
  import AppMenuHeading from "./AppMenuHeading.svelte";
  import AppMenuLink from "./AppMenuLink.svelte";

  export let menuItem: IMenuItem;

  // if (menuItem.loggedIn === undefined) {
  //   menuItem.loggedIn = false;
  // }
</script>

{#if menuItem.loggedIn === undefined || (menuItem.loggedIn === true && isUserAuthed()) || (menuItem.loggedIn === false && !isUserAuthed())}
  {#if menuItem.type === "link"}
    <AppMenuLink {menuItem} />
  {:else if menuItem.type === "heading"}
    <AppMenuHeading {menuItem} />
  {/if}
{/if}
