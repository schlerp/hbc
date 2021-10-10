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

export async function axiosFetch(
  endpoint: string,
  options: AxiosRequestConfig,
  authApiUrl: string = "http://localhost:8004"
) {
  console.log(`${options.method} ${authApiUrl}/${endpoint}`, options.data);
  let response = await axios(`${authApiUrl}/${endpoint}`, options);
  if (response && response.status === 200) {
    return response.data;
  }
  return null;
}

export async function getCompetition(competitionId: number) {
  const method: Method = "GET";
  const options = {
    method: method,
    headers: {
      Accept: "application/json",
    },
  };
  const url = `comp/${competitionId}`;
  return axiosFetch(url, options);
}

export async function getAllCompetitions() {
  const method: Method = "GET";
  const options = {
    method: method,
    headers: {
      Accept: "application/json",
    },
  };
  return axiosFetch("comp", options);
}

// export function upsertUserProfile(userProfile: IUserProfile) {
//   if (userProfile.username !== "") {
//     const method: Method = "PUT";
//     const options = {
//       method: method,
//       headers: {
//         Accept: "application/json",
//       },
//       data: userProfile,
//     };
//     const url = userProfile.username;
//     return axiosFetch(url, options);
//   }
// }
