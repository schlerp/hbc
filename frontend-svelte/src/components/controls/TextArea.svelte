<script lang="ts">
  import genId from "../../utils/genId";

  let control: HTMLTextAreaElement;

  export let value: string = "";
  export let label: string = "Input";
  export let inputId: string = genId();
  export let name: string = inputId;
  export let tabIndex: number = 0;
  export let required: boolean = false;

  if (control !== undefined) {
    control.required = required;
  }
</script>

<div class="form-group">
  <textarea
    bind:this={control}
    bind:value
    id={inputId}
    class="form-control"
    placeholder="text area"
    tabindex={tabIndex}
    {name}
  />
  <label for={inputId} class="form-label">{label}</label>
</div>

<style>
  textarea {
    font-family: inherit;
    font-size: inherit;
  }
  .form-group {
    margin-bottom: var(--spacing);
    transition: all 0.25s;
    /* width: calc(100% - calc(var(--spacing) * 2)); */
    width: 100%;
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
    height: 4.5rem;
    font-size: 1rem;
    transition: all 0.4s;
    resize: none;
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
    transform: translateY(-6.5rem) scale(0.8);
  }
  .form-group:focus-within {
    transform: scale(102%, 102%);
  }
</style>
