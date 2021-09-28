<script type="ts">
  import { getUserFirstName, getUserAvatarUrl } from "../services/profile";
  let userFirstName = getUserFirstName();
  let userAvatarUrl = getUserAvatarUrl();
</script>

<div>
  {#if userFirstName !== undefined}
    <img src={userAvatarUrl} alt={`${userFirstName} avatar`} />
    <span>{userFirstName}</span>
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
    margin: auto;
    justify-content: center;
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
