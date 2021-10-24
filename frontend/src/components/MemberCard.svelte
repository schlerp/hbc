<script lang="ts">
  import { push } from "svelte-spa-router";
  import type { IUserProfile } from "../types";

  console.log("MemberCard loaded...");

  export let profile: IUserProfile;
  export let showAvatar: boolean = true;
  export let showFavouriteStyle: boolean = true;

  function handleClick(username: string) {
    push(`/profile/${username}`);
  }
</script>

<div class="row">
  <div
    class="card"
    on:click={() => {
      handleClick(profile.username);
    }}
  >
    {#if showAvatar === true}
      <img
        class="avatar item"
        src={profile.avatar}
        alt={`${profile.username}'s avatar`}
      />
    {/if}
    <p class="name item">{profile.lastName}, {profile.firstName}</p>
    {#if showFavouriteStyle === true}
      <p class="favStyle item">🍺 {profile.favouriteStyle}</p>
    {/if}
  </div>
</div>

<style>
  .avatar {
    width: calc(var(--spacing) * 15);
    height: calc(var(--spacing) * 15);
    border-radius: 50%;
  }
  .name {
    width: 180px;
  }
  .favStyle {
    width: 120px;
  }
  .row {
    margin: calc(var(--spacing) * 2);
  }
  .card {
    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
    justify-content: center;
    justify-items: center;
    border-radius: var(--spacing);
    box-shadow: 2px 2px 3px 0px var(--pal-text-soft),
      3px 3px 5px 0px var(--pal-text-soft);
    cursor: pointer;
    background-color: #ffffff;
  }
  .item {
    justify-self: center;
    align-self: center;
    margin: calc(var(--spacing) * 2);
    white-space: nowrap;
    overflow: hidden;
    text-overflow: ellipsis;
  }
  .name::before {
    content: "Member Name";
    display: flex;
    top: -1rem;
    color: var(--pal-text-soft);
    font-size: 0.8rem;
  }
  .favStyle::before {
    content: "Favourite Style";
    display: flex;
    top: -1rem;
    color: var(--pal-text-soft);
    font-size: 0.8rem;
  }
</style>
