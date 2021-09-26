<script lang="ts">
  import LandingPage from "./LandingPage.svelte";
  import AppMenu from "./components/menu/AppMenu.svelte";
  import type { IMenuItem } from "./types";

  const menuItems: IMenuItem[] = [
    { text: "Members", type: "heading" },
    { text: "Member List", href: "#/members", type: "link", subtle: true },
    { text: "My Profile", href: "#/profile", type: "link" },
    { text: "Competitions", type: "heading" },
    { text: "All Comps", href: "#/comps", type: "link", subtle: true },
    { text: "My Comps", href: "#/comps/my", type: "link" },
    { text: "My Entries", href: "#/entries ", type: "link" },
  ];
</script>

<main>
  <AppMenu {menuItems} />
  <LandingPage />
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
