<script lang="ts">
  import { userAuth } from "../store/auth";

  export let params;
  let username = null;

  console.log(params);

  if (params.username !== undefined) {
    username = params.username;
  }
</script>

<p>{username}</p>
