<script lang="ts">
  import type { IButtonType } from "../../types";

  import genId from "../../utils/genId";

  let control: HTMLInputElement;

  export let label: string = "Submit";
  export let inputId: string = genId();
  export let name: string = inputId;
  export let tabIndex: number = 0;
  export let type: IButtonType = "secondary";
  export let handleClick = () => {};
	export let disabled = false;
</script>

<button
  {name}
  on:click={handleClick}
  id={inputId}
  class={type}
  tabindex={tabIndex}
	disabled={disabled}
>
  {label}
</button>

<style>
  button {
    box-shadow: none;
    border: none;
    height: 2rem;
    min-width: 6rem;
    border-radius: var(--spacing);
    font-size: 1rem;
    transition: all 50ms;
    cursor: pointer;
  }
  .primary {
    background-color: var(--pal-primary);
    color: var(--pal-text-light);
  }
  .secondary {
    background-color: var(--pal-secondary);
    color: var(--pal-text-dark);
  }
  .info {
    background-color: var(--pal-info);
    color: var(--pal-text-dark);
  }
	button:disabled {
		background-color: var(--pal-info);
		color: var(--pal-text-soft);
	}
  button:active {
    transform: scale(105%);
  }
  button.primary:active {
    background-color: var(--pal-info);
  }
  button.secondary:active {
    background-color: var(--pal-info);
  }
  button.info:active {
    background-color: var(--pal-primary);
  }
</style>
