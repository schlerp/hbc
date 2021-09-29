import { writable } from "svelte/store";
import { isUserAuthed } from "../services/auth";
import { getUserProfile } from "../services/profile";
import type { IUserProfile } from "../types";
import { userAuth } from "./auth";

export const defaultAvatarUrl =
  "https://randomuser.me/api/portraits/lego/1.jpg";

export const emptyUserProfile: IUserProfile = {
  username: null,
  firstName: null,
  lastName: null,
  bio: null,
  avatar: defaultAvatarUrl,
};

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
