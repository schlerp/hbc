import { writable } from "svelte/store";
import { isUserAuthed } from "../services/auth";
import { getUserProfile } from "../services/profile";
import type { IUserProfile } from "../types";
import { userAuth } from "./auth";
import { emptyUserProfile } from "../types";

export const userProfile = writable<IUserProfile>(emptyUserProfile);

userAuth.subscribe(async (localUserAuth) => {
  if (isUserAuthed) {
    const remoteUserProfile = await getUserProfile();
    if (remoteUserProfile !== null) {
      userProfile.set(remoteUserProfile);
    } else {
      userProfile.set(emptyUserProfile);
    }
  }
});
