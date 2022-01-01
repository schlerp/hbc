<script lang="ts">
  import MemberCard from "../components/MemberCard.svelte";
  import ScrollableDiv from "../components/ScrollableDiv.svelte";
  import { getAllProfiles } from "../services/profile";
  import type { IUserProfile } from "../types";

  let memberProfiles: IUserProfile[] = [];
  getAllProfiles().then((profiles) => {
    memberProfiles = profiles;
  });
</script>

<h2>Current Members</h2>
<ScrollableDiv>
  {#each memberProfiles as profile}
    <MemberCard {profile} />
  {/each}
</ScrollableDiv>

<style>
  h2 {
    color: var(--pal-text-dark);
  }
</style>
