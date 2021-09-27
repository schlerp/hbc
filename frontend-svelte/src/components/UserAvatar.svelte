<script type="ts">
  import { getUserFullName, getUserAvatarUrl } from "../services/profile";
  let userFullName = getUserFullName();
  let userAvatarUrl = getUserAvatarUrl();
  console.log(userFullName);
  console.log(userAvatarUrl);
</script>

<div>
  {#if userFullName !== undefined}
    <img src={userAvatarUrl} alt={`${userFullName} avatar`} />
    <span>{userFullName}</span>
  {:else}
    <img
      src="https://randomuser.me/api/portraits/lego/1.jpg"
      alt="Anonymous avatar"
    />
    <span>Anonymous</span>
  {/if}
</div>

<style>
  div {
    display: flex;
    align-items: center;
    /* justify-content: center; */
    padding: calc(var(--spacing) * 1);
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
