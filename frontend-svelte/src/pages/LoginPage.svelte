<script lang="ts">
  import { onDestroy } from "svelte";
  import { push } from "svelte-spa-router";
  import TextInput from "../components/controls/TextInput.svelte";
  import Button from "../components/controls/Button.svelte";
  import { isUserAuthed, login } from "../services/auth";
  import { userAuth } from "../store/auth";

  let username: string = "";
  let password: string = "";

  async function handleSubmit() {
    const loginSuccess = await login(username, password);
    if (loginSuccess) {
      push("/");
    } else {
      console.log("Error logging in!");
      alert("Error logging in!");
      password = "";
    }
  }

  // subscribe to the value for testing
  const unsubscribe = userAuth.subscribe((value) => console.log);

  // don't forget to unsubscribe to stop dem memory leaks
  onDestroy(() => {
    unsubscribe();
  });
</script>

{#if !isUserAuthed()}
  <form on:submit|preventDefault={handleSubmit}>
    <TextInput bind:value={username} label="Username" inputId="username" />
    <TextInput
      bind:value={password}
      label="Password"
      inputId="password"
      inputType="password"
    />
    <Button label="Login" />
  </form>
{:else}
  <h3>Your'e already logged in!</h3>
  <p>Did you mean to <a href="#/logout">Logout</a>?</p>
{/if}

<style>
  form {
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-items: center;
  }
</style>
