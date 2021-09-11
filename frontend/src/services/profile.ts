import axios from "axios";
import authHeader from "./authHeader";

const PROFILE_API_URL = "http://localhost:8002";

const getProfile = (username: string) => {
  return axios.get(PROFILE_API_URL + `/${username}`, { headers: authHeader() });
};

// const getUserBoard = () => {
//   return axios.get(PROFILE_API_URL + "user", { headers: authHeader() });
// };

// const getModeratorBoard = () => {
//   return axios.get(PROFILE_API_URL + "mod", { headers: authHeader() });
// };

// const getAdminBoard = () => {
//   return axios.get(PROFILE_API_URL + "admin", { headers: authHeader() });
// };

export default {
  getProfile,
  //   getUserBoard,
  //   getModeratorBoard,
  //   getAdminBoard,
};
