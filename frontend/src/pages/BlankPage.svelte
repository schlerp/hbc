<script lang="ts">
  import BackgroundAnimation from "../components/BackgroundAnimation.svelte";

  import { config } from "../config";
  export let title = null;
  export let subtitle = null;
</script>

<BackgroundAnimation />
<img src={config.siteLogo} alt={`${config.siteTitle} logo`} />
{#if title !== null}
  <h1>{title}</h1>
{:else}
  <h1>Page Not Found!</h1>
{/if}

{#if subtitle !== null}
  <p>{subtitle}</p>
{/if}

<style>
  h1 {
    text-align: center;
    padding-left: calc(var(--spacing) * 2);
    padding-right: calc(var(--spacing) * 2);
  }
  img {
    max-height: 50%;
    width: clamp(300px, 450px, 80%);
    padding-left: calc(var(--spacing) * 2);
    padding-right: calc(var(--spacing) * 2);
  }
</style>
