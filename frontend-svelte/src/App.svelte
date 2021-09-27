<script lang="ts">
  import LandingPage from "./pages/LandingPage.svelte";
  import LoginPage from "./pages/LoginPage.svelte";
  import AppMenu from "./components/menu/AppMenu.svelte";
  import type { IMenuItem } from "./types";

  const menuItems: IMenuItem[] = [
    { text: "Members", type: "heading" },
    { text: "Member List", href: "#/members", type: "link", subtle: true },
    { text: "My Profile", href: "#/profile", type: "link", loggedIn: true },
    { text: "Competitions", type: "heading" },
    { text: "All Comps", href: "#/comps", type: "link", subtle: true },
    { text: "My Comps", href: "#/comps/my", type: "link", loggedIn: true },
    { text: "My Entries", href: "#/entries ", type: "link", loggedIn: true },
  ];
</script>

<main>
  <AppMenu {menuItems} />
  <!-- <LandingPage /> -->
  <LoginPage />
</main>

<style>
  :root {
    /* CSS theme */
    --spacing: 6px;
    --pal-primary: #a4764f;
    --pal-secondary: #f3b917;
    --pal-info: #f4e9cb;
    --pal-text-dark: #333333;
    --pal-text-light: #fafafa;
    --ff-body: "Montserrat", Roboto, Oxygen-Sans, Ubuntu, Cantarell,
      "Helvetica Neue", sans-serif;
  }
</style>
