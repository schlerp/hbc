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
}

export type IMenuItem = IMenuHeading | IMenuLink;
