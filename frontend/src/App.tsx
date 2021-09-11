import React from "react";
import {
  createTheme,
  makeStyles,
  ThemeProvider,
} from "@material-ui/core/styles";
import { BrowserRouter as Router, Switch, Route, Link } from "react-router-dom";
import NavMenu from "./components/NavMenu";
import { LandingPage } from "./components/LandingPage";
import { UserProfile } from "./components/UserProfilePage";
import { config } from "./config";
import getUser from "./services/getUser";
import SignInPage from "./components/SignInPage";

const theme = createTheme({
  palette: {
    primary: { main: config.sitePalette.primary },
    secondary: { main: config.sitePalette.secondary },
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
  const [user, setUser] = React.useState(null);

  React.useEffect(() => {
    const localUser = getUser();
    if (localUser !== undefined) {
      setUser(localUser);
    }
  }, []);

  return (
    <ThemeProvider theme={theme}>
      <Router>
        <div className={classes.appWrapper}>
          <NavMenu />
          <Switch>
            <Route path="/signin">
              <SignInPage />
            </Route>
            <Route path="/">
              {user === null ? (
                <LandingPage />
              ) : (
                <UserProfile username={user.name} />
              )}
            </Route>
          </Switch>
        </div>
      </Router>
    </ThemeProvider>
  );
}

export default App;
