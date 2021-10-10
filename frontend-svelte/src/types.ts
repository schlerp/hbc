export interface IUserAuth {
  username: string;
  scopes: string[];
  email: string;
  token: string;
}

export interface IUserProfile {
  username: string;
  firstName: string;
  lastName: string;
  bio: string;
  avatar: string;
  active: boolean;
  favouriteStyle: string;
}

export interface ICompetition {
  competitionId: number;
  allowedStyles: string[];
  entriesCloseDate: Date;
  awardsDate: Date;
  description: string;
}

export const defaultAvatarUrl =
  "https://randomuser.me/api/portraits/lego/1.jpg";
export const emptyUserProfile: IUserProfile = {
  username: null,
  firstName: null,
  lastName: null,
  bio: null,
  avatar: defaultAvatarUrl,
  active: true,
  favouriteStyle: null,
};

export interface IMenuHeading {
  text: string;
  type: "heading";
  subheading?: boolean;
  loggedIn?: boolean;
}

export interface IMenuLink {
  text: string;
  href: string;
  icon?: SVGElement;
  type: "link";
  subtle?: boolean;
  loggedIn?: boolean;
}

export type IMenuItem = IMenuHeading | IMenuLink;

export type ITextInputType = "text" | "password";

export type IButtonType = "primary" | "secondary" | "info";
