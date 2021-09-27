import { USER_STORAGE_KEY } from "./auth";

export default function getUser() {
  const user = JSON.parse(localStorage.getItem(USER_STORAGE_KEY));
  console.log("getUser() user:", user);
  if (user !== null) {
    return user;
  }
  return null;
}
