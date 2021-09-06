import React from "react";
import {
  createTheme,
  makeStyles,
  ThemeProvider,
} from "@material-ui/core/styles";
import Button from "./components/controls/Button";
import NavMenu from "./components/NavMenu";

const theme = createTheme();

const useStyles = makeStyles((theme) => ({
  appWrapper: {
    background: theme.palette.primary.main,
    display: "flex",
    flexDirection: "column",
    justifyContent: "center",
    alignItems: "center",
    height: "100%",
    width: "100%",
    color: theme.palette.primary.contrastText,
  },
}));

function App() {
  const classes = useStyles();
  return (
    <ThemeProvider theme={theme}>
      <div className={classes.appWrapper}>
        <NavMenu />
        <h1>ELister</h1>
        <Button label="Add a new List" />
      </div>
    </ThemeProvider>
  );
}

export default App;
