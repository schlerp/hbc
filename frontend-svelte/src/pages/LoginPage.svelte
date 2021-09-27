<script lang="ts">
  console.log("login");
</script>

<form>
  <label for="inputUsername">Username</label>
  <input id="inputUsername" />
  <label for="inputPassword">Password</label>
  <input id="inputPassword" type="password" />
</form>

<style>
  input {
    height: 2rem;
    border-radius: 0.5rem;
    border: 1px solid var(--pal-primary);
  }
  input:focus {
    border: 2px solid var(--pal-secondary);
  }
</style>
