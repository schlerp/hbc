<script lang="ts">
  import genId from "../../utils/genId";
  import type { ITextInputType } from "../../types";

  let control: HTMLInputElement;

  export let value: string = "";
  export let label: string = "Submit";
  export let inputId: string = genId();
  export let name: string = inputId;
  export let tabIndex: number = 0;
</script>

<button {name} id={inputId} class="form-control" tabindex={tabIndex}>
  {label}
</button>

<style>
  button {
    box-shadow: none;
    background-color: var(--pal-secondary);
    height: 2rem;
    min-width: 8rem;
    border-radius: var(--spacing);
    font-size: 1rem;
    transition: all 50ms;
  }
  button:active {
    transform: scale(105%);
    background-color: var(--pal-info);
  }
</style>
