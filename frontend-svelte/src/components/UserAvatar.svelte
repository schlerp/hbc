<script type="ts">
  import { push } from "svelte-spa-router";

  import { getUserFirstName, getUserAvatarUrl } from "../services/profile";
  import { getUserName } from "../services/auth";
  import Button from "./controls/Button.svelte";
  let userFirstName = getUserFirstName();
  let userAvatarUrl = getUserAvatarUrl();

  function handleAvatarClick() {
    if (userFirstName !== undefined) {
      push(`/profile/${getUserName()}`);
    } else {
      push("/login");
    }
  }

  function handleRegisterClick() {
    push("/register");
  }

  function handleLoginClick() {
    push("/login");
  }
</script>

{#if userFirstName !== undefined}
  <div class="avatarWrapper" on:click={handleAvatarClick}>
    <img src={userAvatarUrl} alt={`${userFirstName} avatar`} />
    <span>{userFirstName}</span>
  </div>
{:else}
  <div>
    <img
      src="https://randomuser.me/api/portraits/lego/1.jpg"
      alt="anonymous avatar"
    />
    <span>Anonymous</span>
  </div>
  <div>
    <Button label="Register" type="info" handleClick={handleRegisterClick} />
    <Button label="Log in" type="primary" handleClick={handleLoginClick} />
  </div>
{/if}

<style>
  div {
    display: flex;
    align-items: center;
    margin: var(--spacing);
    justify-content: center;
    padding: calc(var(--spacing) * 1);
    cursor: pointer;
    color: var(--pal-text-dark);
    margin: var(--spacing);
    gap: var(--spacing);
  }
  img {
    height: calc(var(--spacing) * 10);
    width: calc(var(--spacing) * 10);
    border-radius: 50%;
  }
  span {
    font-size: 1.5rem;
    padding: var(--spacing);
  }
</style>
