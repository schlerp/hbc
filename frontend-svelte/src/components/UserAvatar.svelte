<script type="ts">
  import { getUserFullName, getUserAvatarUrl } from "../services/user";
  export let currentUsername: string;
  let userFullName = getUserFullName(currentUsername);
  let userAvatarUrl = getUserAvatarUrl(userFullName);
</script>

<div>
  <img src={userAvatarUrl} alt={`${currentUsername} avatar image`} />
  <span>{userFullName}</span>
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
