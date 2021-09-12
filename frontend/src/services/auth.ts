export const API_URL = "http://localhost:8001";
export const USER_STORAGE_KEY = "current_user";

const register = (username: string, email: string, password: string) => {
  return fetch(API_URL + "/signup", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({
      username,
      email,
      password,
    }),
  });
};

const login = (username: string, password: string) => {
  console.log(
    JSON.stringify({
      username: username,
      password: password,
    })
  );
  return fetch(API_URL + "/login", {
    method: "POST",
    mode: "cors",
    headers: {
      "Content-Type": "application/json",
      Accept: "application/json",
    },
    body: JSON.stringify({
      username: username,
      password: password,
    }),
  })
    .then((response) => {
      return response.json();
    })
    .then((json) => {
      if (json.token) {
        localStorage.setItem(USER_STORAGE_KEY, JSON.stringify(json));
      }
      return json;
    })
    .catch((error) => console.log(error));
};

const logout = () => {
  localStorage.removeItem(USER_STORAGE_KEY);
};

const getCurrentUser = () => {
  return JSON.parse(localStorage.getItem(USER_STORAGE_KEY));
};

export default {
  register,
  login,
  logout,
  getCurrentUser,
};
