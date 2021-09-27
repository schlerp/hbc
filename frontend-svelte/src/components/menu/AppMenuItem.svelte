<script lang="ts">
  import { debug } from "svelte/internal";

  import { isUserAuthed } from "../../services/auth";
  import type { IMenuItem } from "../../types";
  import AppMenuHeading from "./AppMenuHeading.svelte";
  import AppMenuLink from "./AppMenuLink.svelte";

  export let menuItem: IMenuItem;
  console.log(menuItem);
  console.log(isUserAuthed());
</script>

{#if menuItem.type === "heading"}
  <AppMenuHeading {menuItem} />
{:else if menuItem.loggedIn !== undefined && menuItem.loggedIn === true && isUserAuthed()}
  <AppMenuLink {menuItem} />
{:else if menuItem.loggedIn === undefined || menuItem.loggedIn === false}
  <AppMenuLink {menuItem} />
{/if}
