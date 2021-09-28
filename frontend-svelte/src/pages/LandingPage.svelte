<script lang="ts">
  import { config } from "../config";

  export const params = null;

  document.title = config.siteTitle;
</script>

<img src={config.siteLogo} alt={`${config.siteTitle} logo`} />
<h1>{config.siteTitle}</h1>

<style>
  h1 {
    text-align: center;
    padding-left: calc(var(--spacing) * 2);
    padding-right: calc(var(--spacing) * 2);
  }
  img {
    max-height: 50%;
    width: auto;
    padding-left: calc(var(--spacing) * 2);
    padding-right: calc(var(--spacing) * 2);
  }
</style>
