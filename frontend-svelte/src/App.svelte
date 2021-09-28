<script lang="ts">
  import LandingPage from "./pages/LandingPage.svelte";
  import Router, { location, push } from "svelte-spa-router";
  import LoginPage from "./pages/LoginPage.svelte";
  import AppMenu from "./components/menu/AppMenu.svelte";
  import type { IMenuItem } from "./types";
  import { logout } from "./services/auth";
  import { config } from "./config";
  import NotFound from "./pages/NotFound.svelte";

  document.title = config.siteTitle;

  const logoutUrl: string = "/logout";

  const menuItems: IMenuItem[] = [
    {
      text: "Login",
      href: "#/login",
      type: "link",
      loggedIn: false,
    },
    {
      text: "Logout",
      href: `#${logoutUrl}`,
      type: "link",
      loggedIn: true,
    },
    { text: "Members", type: "heading" },
    { text: "Member List", href: "#/members", type: "link", subtle: true },
    { text: "My Profile", href: "#/profile", type: "link", loggedIn: true },
    { text: "Competitions", type: "heading" },
    { text: "All Comps", href: "#/comps", type: "link", subtle: true },
    { text: "My Comps", href: "#/comps/my", type: "link", loggedIn: true },
    { text: "My Entries", href: "#/entries ", type: "link", loggedIn: true },
  ];

  const routes = {
    "/": LandingPage,
    "/login": LoginPage,
    "*": NotFound,
  };

  console.log($location);

  location.subscribe((value) => {
    console.log(value);
    if (value === logoutUrl) {
      logout();
      console.log("logged out!");
      push("/");
    }
  });
</script>

<main>
  <AppMenu {menuItems} />
  <Router {routes} />
  <!-- <LandingPage /> -->
  <!-- <LoginPage /> -->
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
