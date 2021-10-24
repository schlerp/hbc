<script lang="ts">
  import { userAuth } from "../store/auth";
  import { getUserProfile, upsertUserProfile } from "../services/profile";
  import type { IUserProfile } from "../types";
  import TextInput from "../components/controls/TextInput.svelte";
  import { emptyUserProfile } from "../types";
  import TextArea from "../components/controls/TextArea.svelte";
  import Button from "../components/controls/Button.svelte";

  export let params;
  let currentUsername: string = null;
  let canEdit: boolean = false;
  let currentProfile: IUserProfile = emptyUserProfile;

  userAuth.subscribe((value) => {
    currentUsername = value.username;
  });

  if (params.username === currentUsername) {
    canEdit = true;
  }

  if (params.username !== null) {
    console.log(params.username);
    getUserProfile(params.username).then((data) => {
      console.log(data);
      if (data !== null) {
        currentProfile = data;
      }
    });
  }

  function handleProfileUpdate() {
    console.log(currentProfile);
    if (currentProfile.username === null) {
      currentProfile.username = params.username;
    }
    upsertUserProfile(currentProfile);
  }
</script>

<div class="wrapper">
  {#if canEdit}
    <form on:submit|preventDefault={handleProfileUpdate}>
      <img src={currentProfile.avatar} alt={`${currentUsername}'s avatar`} />
      <h2>{params.username}'s Profile</h2>
      <TextInput
        name="firstName"
        label="First Name"
        bind:value={currentProfile.firstName}
      />
      <TextInput
        name="LastName"
        label="Last Name"
        bind:value={currentProfile.lastName}
      />
      <TextArea name="bio" label="Biography" bind:value={currentProfile.bio} />
      <TextInput
        name="avatar"
        label="Avatar"
        bind:value={currentProfile.avatar}
      />
      <Button label="Update Profile" />
    </form>
  {:else if currentProfile !== emptyUserProfile}
    <img src={currentProfile.avatar} alt={`${currentUsername}'s avatar`} />
    <h2>{params.username}'s Profile</h2>
    <p>
      <strong>{currentProfile.firstName} {currentProfile.lastName} </strong>
    </p>
    <p>{currentProfile.bio}</p>
  {:else}
    <h2>{params.username}'s Profile</h2>
    <p>{params.username} does not have a profile!</p>
  {/if}
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
</style>
