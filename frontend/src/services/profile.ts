import { IUserProfile } from "../types";
import authHeader from "./authHeader";

const PROFILE_API_URL = "http://localhost:8002";
const PROFILE_STORAGE_KEY = "current_profile";

const getLocalProfile = () => {
  return JSON.parse(localStorage.getItem(PROFILE_STORAGE_KEY));
};

const getProfile = async (username: string) => {
  return await fetch(PROFILE_API_URL + `/${username}`, {
    headers: authHeader(),
  }).then((resp) => {
    return resp.json();
  });
};

const updateCachedProfile = (username: string) => {
  fetch(PROFILE_API_URL + `/${username}`, {
    headers: authHeader(),
  })
    .then((resp) => {
      return resp.json();
    })
    .then((json) => {
      localStorage.setItem(PROFILE_STORAGE_KEY, JSON.stringify(json));
    })
    .catch(console.log);
};

const updateProfile = async (profile: IUserProfile) => {
  return fetch(PROFILE_API_URL + `/profile`, {
    method: "PUT",
    mode: "cors",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
      ...authHeader(),
    },
    body: JSON.stringify(profile),
  });
};

export default {
  getLocalProfile,
  getProfile,
  updateCachedProfile,
  updateProfile,
};
