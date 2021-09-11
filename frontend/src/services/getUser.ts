import { USER_STORAGE_KEY } from "./auth";

export default function getUser() {
  const user = JSON.parse(localStorage.getItem(USER_STORAGE_KEY));

  if (user && user.accessToken) {
    const decodedToken = JSON.parse(
      Buffer.from(user.accessToken.split(".")[1], "base64").toString()
    );
    return decodedToken.name;
  }
}
