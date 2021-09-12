import React from "react";
import { makeStyles } from "@material-ui/core";
import { TextField } from "@material-ui/core";
import Button from "./controls/Button";
import authClient from "../services/auth";
import { config } from "../config";
import { useHistory } from "react-router";

const useStyles = makeStyles((theme) => ({
  form: {
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    alignItems: "center",
  },
  formElement: {
    margin: theme.spacing(1),
    // width: "25ch",
  },
  heading: {
    textAlign: "center",
    paddingLeft: theme.spacing(2),
    paddingRight: theme.spacing(2),
  },
  image: {
    height: "33%",
  },
}));

interface ISignInPageProps {
  setLoggedIn: Function;
}

export const SignInPage: React.FC<ISignInPageProps> = ({ setLoggedIn }) => {
  const classes = useStyles();
  const history = useHistory();

  async function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    const target = event.target as typeof event.target & {
      username: { value: string };
      password: { value: string };
    };
    const username = target.username.value;
    const password = target.password.value;
    await authClient.login(username, password);
    setLoggedIn(true);
    history.push(`/profile/${username}`);
  }

  return (
    <>
      <img className={classes.image} src={config.siteLogo} />
      <h1 className={classes.heading}>{config.siteTitle}</h1>
      <form className={classes.form} onSubmit={handleSubmit}>
        <TextField
          className={classes.formElement}
          label="Username"
          name="username"
          variant="outlined"
        />
        <TextField
          className={classes.formElement}
          label="Password"
          name="password"
          type="password"
          variant="outlined"
        />
        <Button className={classes.formElement} label="Sign in" />
      </form>
    </>
  );
};

export default SignInPage;
