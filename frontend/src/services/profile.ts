import axios, { AxiosRequestConfig, Method } from "axios";
import { get } from "svelte/store";
import { emptyUserAuth, userAuth } from "../store/auth";
import { userProfile } from "../store/profile";
import type { IUserProfile } from "../types";
import { isUserAuthed } from "./auth";
import { emptyUserProfile, defaultAvatarUrl } from "../types";

var localUserAuth = emptyUserAuth;
var localUserProfile = emptyUserProfile;

userAuth.subscribe((value) => {
  localUserAuth = value;
});

userProfile.subscribe((value) => {
  localUserProfile = value;
});


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

export async function axiosFetch(
  endpoint: string,
  options: AxiosRequestConfig,
  authApiUrl: string = "http://localhost:8002"
) {
  console.log(`${options.method} ${authApiUrl}/${endpoint}`, options.data);
  let response = await axios(`${authApiUrl}/${endpoint}`, options);
  if (response && response.status === 200) {
    return response.data;
  }
  return null;
}

export async function getUserProfile(
  username: string = get(userAuth).username
) {
  if (username !== "") {
    const method: Method = "GET";
    const options = {
      method: method,
      headers: {
        Accept: "application/json",
      },
    };
    const url = username;
    return axiosFetch(url, options);
  }
}

export async function getAllProfiles() {
  const method: Method = "GET";
  const options = {
    method: method,
    headers: {
      Accept: "application/json",
    },
  };
  return axiosFetch("profile", options);
}

export function getUserFirstName() {
  if (isUserAuthed() && localUserProfile !== emptyUserProfile) {
    return localUserProfile.firstName;
  } else if (isUserAuthed() && localUserProfile === emptyUserProfile) {
    return localUserAuth.username;
  }
}

export function getUserAvatarUrl() {
  console.log(localUserProfile);
  if (isUserAuthed() && localUserProfile !== null) {
    return localUserProfile.avatar;
  } else if (isUserAuthed() && localUserProfile === null) {
    return defaultAvatarUrl;
  }
}

export function upsertUserProfile(userProfile: IUserProfile) {
  if (userProfile.username !== "") {
    const method: Method = "PUT";
    const options = {
      method: method,
      headers: {
        Accept: "application/json",
      },
      data: userProfile,
    };
    const url = userProfile.username;
    return axiosFetch(url, options);
  }
}
