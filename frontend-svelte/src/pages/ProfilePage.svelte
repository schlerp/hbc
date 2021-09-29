<script lang="ts">
  import { userAuth } from "../store/auth";
  import { getUserProfile, upsertUserProfile } from "../services/profile";
  import type { IUserProfile } from "../types";
  import TextInput from "../components/controls/TextInput.svelte";
  import { emptyUserProfile } from "../store/profile";
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

<h3>{params.username}'s Profile</h3>
{#if canEdit}
  <form on:submit|preventDefault={handleProfileUpdate}>
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
  <p><strong>{currentProfile.firstName} {currentProfile.lastName} </strong></p>
  <p>{currentProfile.bio}</p>
{:else}
  <p>{params.username} does not have a profile!</p>
{/if}

<style>
  form {
    display: flex;
    flex-direction: column;
    justify-items: center;
    align-items: center;
  }
</style>
