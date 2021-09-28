import { writable } from "svelte/store";
import { isUserAuthed } from "../services/auth";
import { getUserProfile } from "../services/profile";
import type { IUserProfile } from "../types";
import { userAuth } from "./auth";

const emptyUserProfile: IUserProfile = {
  username: null,
  firstName: null,
  lastName: null,
  bio: null,
  avatar: null,
};

export const userProfile = writable<IUserProfile>();

userAuth.subscribe(async (localUserAuth) => {
  if (isUserAuthed) {
    const remoteUserProfile = await getUserProfile();
    userProfile.set(remoteUserProfile);
  }
});
