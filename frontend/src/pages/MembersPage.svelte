<script lang="ts">
  import { push } from "svelte-spa-router";
  import MemberCard from "../components/MemberCard.svelte";
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
    <MemberCard {profile} />
  {/each}
</div>

<style>
  h2 {
    color: var(--pal-text-dark);
  }
</style>
