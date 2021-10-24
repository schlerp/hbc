import { writable } from "svelte/store";
import type { IUserAuth } from "../types";

export const emptyUserAuth = {
  username: "",
  scopes: [],
  email: "",
  token: "",
};

export const userAuth = writable<IUserAuth>(emptyUserAuth);
