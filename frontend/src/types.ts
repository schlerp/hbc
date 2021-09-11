interface ILogin {
  username: string;
  password: string;
}

export interface IAuthApiClient extends Promise<Object> {
  login(args: ILogin): Function;
  signup(args: ILogin): Function;
}
