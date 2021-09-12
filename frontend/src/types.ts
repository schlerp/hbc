interface ILogin {
  username: string;
  password: string;
}

export interface IAuthApiClient extends Promise<Object> {
  login(args: ILogin): Function;
  signup(args: ILogin): Function;
}

export interface IUserInStorage {
  username: string;
  scopes: Array<string>;
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
