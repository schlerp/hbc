<script lang="ts">
  import type { IMenuLink } from "../../types";
  export let menuItem: IMenuLink;
</script>

{#if menuItem.subtle === undefined || menuItem.subtle === false}
  <a href={menuItem.href}><li class="bright">{menuItem.text}</li></a>
{:else}
  <a href={menuItem.href}><li class="subtle">{menuItem.text}</li></a>
{/if}

<style>
  li {
    padding: calc(var(--spacing) * 2);
    margin-bottom: var(--spacing);
    text-align: center;
    border-radius: var(--spacing);
  }
  li.bright {
    background-color: var(--pal-info);
    color: var(--pal-text-dark);
  }
  li.subtle {
    background-color: var(--pal-primary);
    color: var(--pal-text-light);
  }
  a {
    text-decoration: none;
    color: var(--pal-text-light);
  }
</style>
