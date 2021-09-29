import axios, { AxiosRequestConfig, Method } from "axios";
import { userAuth, emptyUserAuth } from "../store/auth";

var localUserAuth = null;
export const localStorageAuthKey = "hbc_auth";

userAuth.subscribe((value) => {
  localUserAuth = value;
});

export async function axiosFetch(
  endpoint: string,
  options: AxiosRequestConfig,
  authApiUrl: string = "http://localhost:8001"
) {
  let response = await axios(`${authApiUrl}/${endpoint}`, options).catch(
    console.log
  );
  if (response && response.status === 200) {
    return response.data;
  }
  return null;
}

export async function login(username: string, password: string) {
  const method: Method = "POST";
  const options = {
    method: method,
    mode: "cors",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
    data: {
      username: username,
      password: password,
    },
  };

  const loginSuccess = await axiosFetch("login", options).then((json) => {
    if (json !== null) {
      userAuth.set(json);
      localStorage.setItem(localStorageAuthKey, JSON.stringify(json));
      return true;
    } else {
      return false;
    }
  });
  return loginSuccess;
}

export function isUserAuthed() {
  return localUserAuth !== emptyUserAuth;
}

export function logout() {
  userAuth.set(emptyUserAuth);
  localStorage.removeItem(localStorageAuthKey);
}

export function getUserName() {
  if (isUserAuthed()) {
    return localUserAuth.username;
  }
  return null;
}

// export async function register(
//   username: string,
//   email: string,
//   password: string
// ) {
//   return fetch(API_URL + "/signup", {
//     method: "POST",
//     headers: {
//       "Content-Type": "application/json",
//     },
//     body: JSON.stringify({
//       username,
//       email,
//       password,
//     }),
//   });
// }
