<script lang="ts">
  import { push } from "svelte-spa-router";

  import { getAllProfiles } from "../services/profile";
  import type { IUserProfile } from "../types";

  let memberProfiles: IUserProfile[] = [];
  getAllProfiles().then((profiles) => {
    memberProfiles = profiles;
  });

  function handleClick(username: string) {
    push(`/profile/${username}`);
  }
</script>

<h2>Current Members</h2>
<div>
  {#each memberProfiles as profile}
    <div
      class="row"
      on:click={() => {
        handleClick(profile.username);
      }}
    >
      <img
        class="col1 item"
        src={profile.avatar}
        alt={`${profile.username}'s avatar`}
      />
      <p class="col2 item">{profile.lastName}, {profile.firstName}</p>
      <p class="col3 item">🍺 {profile.favouriteStyle}</p>
    </div>
  {/each}
</div>

<style>
  h2 {
    color: var(--pal-text-dark);
  }
  img {
    width: calc(var(--spacing) * 15);
    height: calc(var(--spacing) * 15);
    border-radius: 50%;
  }
  p {
    font-size: 1rem;
  }
  .row {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
    justify-items: center;
    margin: calc(var(--spacing) * 2);
    /* border: 1px solid salmon; */
    border-radius: var(--spacing);
    box-shadow: 2px 2px 3px 0px var(--pal-text-soft),
      3px 3px 5px 0px var(--pal-text-soft);
    cursor: pointer;
  }
  .item {
    justify-self: center;
    align-self: center;
    margin: calc(var(--spacing) * 2);
  }
  .col2::before {
    content: "Name";
    display: flex;
    align-items: center;
    justify-content: center;
    top: -1rem;
    color: var(--pal-text-soft);
    font-size: 0.8rem;
  }
  .col3::before {
    content: "Style";
    display: flex;
    align-items: center;
    justify-content: center;
    top: -1rem;
    color: var(--pal-text-soft);
    font-size: 0.8rem;
  }
</style>
