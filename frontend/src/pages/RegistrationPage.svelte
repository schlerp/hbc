<script lang="ts">
  import { userAuth } from "../store/auth";
  import type { IUserAuth } from "../types";
  import TextInput from "../components/controls/TextInput.svelte";
  import TextArea from "../components/controls/TextArea.svelte";
  import Button from "../components/controls/Button.svelte";
  import { passwordStrength as checkPassword , Result as PasswordResult} from 'check-password-strength'

  let username: string = '';
  let password: string = '';
  let passwordVerify: string = '';
  let email: string = '';
  let passwordStrength: PasswordResult = {id: 0}
  let valid = false;
  let passwordVerifyElem: HTMLInputElement;

  $: passwordStrength = checkPassword(password);
  $: validatePasswordsMatch(password, passwordVerify);
  $: valid = passwordStrength.id >= 3 && password === passwordVerify && !!email.length && !!username.length;


  function validatePasswordsMatch(password1, password2) {
    if(!passwordVerifyElem) {
      return;
    }
    console.log('elem', passwordVerifyElem);
    passwordVerifyElem.setCustomValidity(password1 === password2
      ? ''
      : 'Passwords do not match'
      );
  }

  function handleChangePassword(input: HtmlInputElement) {
    console.log(input);
    console.log('password', password);
    passwordStrength = parseFloat(checkPassword(password));
  }

  function handleRegisterUser() {
    console.log('Register user');
  }
</script>

<div class="wrapper">
    <form on:submit|preventDefault={handleRegisterUser}>
      <h2>Register new account</h2>
      <TextInput
        name="username"
        label="Username"
        bind:value={username}
      />
      <TextInput
        name="email"
        label="Email"
        bind:value={email}
        />
      <TextInput
        inputType="password"
        name="password"
        label="Password"
        bind:value={password}
      />
      <TextInput
        inputType="password"
        name="password2"
        label="Verify Password"
        bind:value={passwordVerify}
        bind:control={passwordVerifyElem}
      />
			<meter max="5" min="0" low="2" high="5" optimum="4" value={password ? passwordStrength.id + 1 : 0}></meter>
      <Button label="Register" disabled={!valid} />

    </form>
</div>

<style>
  form {
    display: flex;
    flex-direction: column;
    justify-items: center;
    align-items: center;
    padding: var(--spacing);
    width: 100%;
  }
  img {
    height: calc(var(--spacing) * 15);
    width: calc(var(--spacing) * 15);
    border-radius: 50%;
  }
  .wrapper {
    display: flex;
    flex-direction: column;
    justify-items: center;
    align-items: center;
    max-width: 600px;
    width: clamp(300px, 50%, 600px);
    padding: var(--spacing);
    margin: calc(var(--spacing) * 2);
    border-radius: var(--spacing);
    box-shadow: 2px 2px 3px 0px var(--pal-text-soft),
      3px 3px 5px 0px var(--pal-text-soft);
  }
	meter {
		-moz-appearance: none;
		-webkit-appearance: none;
		width: 100%;
		height: 50%;
		border-radius: var(--spacing);
		background: var(--pal-super-light);


		margin-bottom: var(--spacing);
		transition: all 0.25s;
		width: calc(100% - calc(var(--spacing) * 4));
	}
	meter::-webkit-meter-optimum-value {
	}
	meter::-webkit-meter-suboptimum-value {
	}
	meter::-webkit-meter-even-less-good-value {
		background: blue;
	}
	-moz-meter-sub-sub-optimum::-moz-meter-bar {
		background: red;
	}
	-moz-meter-sub-optimum::-moz-meter-bar {
		background: yellow;
	}
</style>
