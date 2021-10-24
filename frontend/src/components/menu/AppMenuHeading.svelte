<script lang="ts">
  import type { IMenuHeading } from "../../types";
  export let menuItem: IMenuHeading;
</script>

{#if menuItem.subheading === undefined || menuItem.subheading === true}
  <h3>{menuItem.text}</h3>
{:else}
  <h4>{menuItem.text}</h4>
{/if}

<style>
  h3,
  h4 {
    text-align: center;
    color: var(--pal-text-dark);
  }
</style>
