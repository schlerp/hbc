import { USER_STORAGE_KEY } from "./auth";

export default function getUser() {
  const user = JSON.parse(localStorage.getItem(USER_STORAGE_KEY));

  if (user) {
    return user;
  }
  return null;
}
