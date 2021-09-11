import { USER_STORAGE_KEY } from "./auth";

export default function authHeader() {
  const user = JSON.parse(localStorage.getItem(USER_STORAGE_KEY));

  if (user && user.accessToken) {
    return { Authorization: "Bearer " + user.accessToken };
  } else {
    return {};
  }
}
