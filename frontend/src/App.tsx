import React from "react";
import {
  createTheme,
  makeStyles,
  ThemeProvider,
} from "@material-ui/core/styles";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import NavMenu from "./components/NavMenu";
import { LandingPage } from "./components/LandingPage";
import { UserProfilePage } from "./components/UserProfilePage";
import { config } from "./config";
import getUser from "./services/getUser";
import SignInPage from "./components/SignInPage";
import { IUserInStorage } from "./types";
import profile from "./services/profile";

const theme = createTheme({
  palette: {
    primary: { main: config.sitePalette.primary },
    secondary: { main: config.sitePalette.secondary },
    info: { main: config.sitePalette.info },
  },
});

const useStyles = makeStyles((theme) => ({
  appWrapper: {
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    alignItems: "center",
    height: "100%",
    width: "100%",
  },
}));

function App() {
  const classes = useStyles();
  const [user, setUser] = React.useState<IUserInStorage>(null);
  const [loggedIn, setLoggedIn] = React.useState(false);

  React.useEffect(() => {
    if (loggedIn) {
      const localUser = getUser();
      console.log(localUser);
      if (localUser !== undefined) {
        setUser(localUser);
      }
      profile.updateCachedProfile(localUser.username);
    }
  }, [loggedIn]);

  return (
    <ThemeProvider theme={theme}>
      <Router>
        <div className={classes.appWrapper}>
          <NavMenu currentUser={user} />
          <Switch>
            <Route path="/signin">
              <SignInPage setLoggedIn={setLoggedIn} />
            </Route>
            <Route path="/profile/:targetUsername">
              <UserProfilePage />
            </Route>
            <Route path="/">
              <LandingPage />
            </Route>
          </Switch>
        </div>
      </Router>
    </ThemeProvider>
  );
}

export default App;
