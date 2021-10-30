import { writable } from "svelte/store";
import { isUserAuthed } from "../services/auth";
import type { IUserProfile } from "../types";
import { userAuth } from "./auth";
import { emptyUserProfile } from "../types";

export const userProfile = writable<IUserProfile>(emptyUserProfile);
