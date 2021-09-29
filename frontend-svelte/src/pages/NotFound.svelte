<script lang="ts">
  import { config } from "../config";
  export const params = null;
</script>

<img src={config.siteLogo} alt={`${config.siteTitle} logo`} />
<h1>Page Not Found!</h1>

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
