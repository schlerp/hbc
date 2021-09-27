import { writable } from "svelte/store";
import { isUserAuthed } from "../services/auth";
import { getUserProfile } from "../services/profile";
import type { IUserProfile } from "../types";
import { userAuth } from "./auth";

export const userProfile = writable<IUserProfile>({
  username: null,
  first_name: null,
  last_name: null,
  bio: null,
  avatar: null,
});

userAuth.subscribe(async (localUserAuth) => {
  if (isUserAuthed) {
    const remoteUserProfile = await getUserProfile();
    userProfile.set(remoteUserProfile);
  }
});
