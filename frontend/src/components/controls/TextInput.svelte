<script lang="ts">
  import genId from "../../utils/genId";
  import type { ITextInputType } from "../../types";

  export let control: HTMLInputElement;

  export let value: string = "";
  export let label: string = "Input";
  export let inputType: ITextInputType = "text";
  export let inputId: string = genId();
  export let name: string = inputId;
  export let tabIndex: number = 0;
  export let required: boolean = false;

  if (control !== undefined) {
    control.required = required;
  }
</script>

<div class="form-group">
  {#if inputType === "password"}
    <input
      bind:this={control}
      bind:value
      id={inputId}
      type="password"
      class="form-control"
      placeholder="input control"
      tabindex={tabIndex}
      {name}
    />
  {:else}
    <input
      bind:this={control}
      bind:value
      id={inputId}
      type="text"
      class="form-control"
      placeholder="input control"
      tabindex={tabIndex}
      {name}
    />
  {/if}
  <label for={inputId} class="form-label">{label}</label>
</div>

<style>
  input {
    width: 100%;
  }
	input:invalid {
		background-color: var(--pal-danger);
	}
  .form-group {
    margin-bottom: var(--spacing);
    transition: all 0.25s;
    width: calc(100% - calc(var(--spacing) * 4));
  }
  .form-label {
    font-size: 1rem;
    padding-left: var(--spacing);
    padding-right: var(--spacing);
    color: var(--pal-text-dark);
    display: block;
    transform: translateY(-1.75rem);
    transform-origin: 0 0;
    transition: all 0.25s;
  }
  .form-control {
    box-shadow: none;
    /* background-color: var(--pal-info); */
    background-color: #fafafa;
    padding: var(--spacing);
    border-radius: var(--spacing);
    border-color: var(--pal-info);
    border-style: none none solid none;
    width: calc(100% - calc(var(--spacing) * 2));
    /* width: 300px; */
    height: 1.5em;
    font-size: 1em;
    transition: all 0.4s;
  }
  .form-control::placeholder {
    color: rgba(0, 0, 0, 0);
  }
  .form-control:focus {
    box-shadow: none;
    outline: none;
    border-color: var(--pal-secondary);
  }
  .form-control:focus + .form-label,
  .form-control:not(:placeholder-shown) + .form-label {
    transform: translateY(-3.5rem) scale(0.8);
  }
  /* .form-group:focus-within {
    transform: scale(102%, 102%);
  } */
</style>
