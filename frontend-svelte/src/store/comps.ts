import { writable } from "svelte/store";
import type { ICompetition, IUserAuth } from "../types";

export const competitions = writable<ICompetition[]>([]);
