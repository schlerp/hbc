<script lang="ts">
</script>

<div>
  <slot />
</div>

<style>
  div {
    overflow-y: scroll;
    -ms-overflow-style: none;
    scrollbar-width: none;
  }
  div::-webkit-scrollbar {
    display: none;
  }
</style>
