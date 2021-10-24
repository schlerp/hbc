<script lang="ts">
  import { onDestroy } from "svelte";
  import LandingPage from "./pages/LandingPage.svelte";
  import Router, { location, push } from "svelte-spa-router";
  import LoginPage from "./pages/LoginPage.svelte";
  import AppMenu from "./components/menu/AppMenu.svelte";
  import type { IMenuItem } from "./types";
  import { localStorageAuthKey, logout } from "./services/auth";
  import { config } from "./config";
  import NotFound from "./pages/BlankPage.svelte";
  import ProfilePage from "./pages/ProfilePage.svelte";
  import { userAuth } from "./store/auth";
  import MembersPage from "./pages/MembersPage.svelte";
  import CompetitionsPage from "./pages/CompetitionsPage.svelte";

  const logoutUrl: string = "/logout";

  let username = null;
  let menuItems: IMenuItem[];
  const unsubscribe = userAuth.subscribe((value) => {
    username = value.username;
  });

  menuItems = [
    {
      text: "Logout",
      href: `#${logoutUrl}`,
      type: "link",
      loggedIn: true,
    },
    { text: "News", type: "heading" },
    { text: "Latest News", href: "#/news", type: "link", subtle: true },
    { text: "Members", type: "heading" },
    { text: "Member List", href: "#/members", type: "link", subtle: true },
    { text: "Competitions", type: "heading" },
    { text: "All Comps", href: "#/comps", type: "link", subtle: true },
    { text: "My Entries", href: "#/entries ", type: "link", loggedIn: true },
  ];

  const routes = {
    "/": LandingPage,
    "/login": LoginPage,
    "/profile/:username?": ProfilePage,
    "/members": MembersPage,
    "/comps": CompetitionsPage,
    "*": NotFound,
  };

  document.title = config.siteTitle;

  location.subscribe((value) => {
    console.log(value);
    if (value === logoutUrl) {
      logout();
      console.log("logged out!");
      push("/");
    }
  });

  // check if user already logged in (in localStorage)
  const storedUserAuth = localStorage.getItem(localStorageAuthKey);
  if (storedUserAuth !== null) {
    userAuth.set(JSON.parse(storedUserAuth));
  }

  onDestroy(() => {
    unsubscribe();
  });
</script>

<main>
  <AppMenu {menuItems} />
  <Router {routes} />
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
    --pal-text-soft: #cccccc;
    --ff-body: "Montserrat", Oxygen-Sans, "Helvetica Neue", sans-serif;
  }
</style>
