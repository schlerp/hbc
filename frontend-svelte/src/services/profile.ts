import axios, { AxiosRequestConfig, Method } from "axios";
import { get } from "svelte/store";
import { userAuth } from "../store/auth";
import { userProfile } from "../store/profile";
import { isUserAuthed } from "./auth";

var localUserAuth = null;
var localUserProfile = null;

userAuth.subscribe((value) => {
  localUserAuth = value;
});

userProfile.subscribe((value) => {
  localUserProfile = value;
});

export async function axiosFetch(
  endpoint: string,
  options: AxiosRequestConfig,
  authApiUrl: string = "http://localhost:8002"
) {
  console.log(`${authApiUrl}/${endpoint}`);
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

export function getUserFirstName() {
  if (isUserAuthed()) {
    return localUserProfile.firstName;
  }
}

export function getUserAvatarUrl() {
  if (isUserAuthed()) {
    return localUserProfile.avatar;
  }
}
