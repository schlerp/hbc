export interface IUserAuth {
  username: string;
  scopes: string[];
  email: string;
  token: string;
}

export interface IUserProfile {
  username: string;
  first_name: string;
  last_name: string;
  bio: string;
  avatar: string;
}

export interface IMenuHeading {
  text: string;
  type: "heading";
  subheading?: boolean;
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
