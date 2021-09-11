import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Button from "./controls/Button";
import { config } from "../config";

const useStyles = makeStyles((theme) => ({
  heading: {
    textAlign: "center",
    paddingLeft: theme.spacing(2),
    paddingRight: theme.spacing(2),
  },
  image: {
    height: "50%",
  },
}));

export const LandingPage: React.FC = () => {
  const classes = useStyles();
  return (
    <>
      <img className={classes.image} src={config.siteLogo} />
      <h1 className={classes.heading}>{config.siteTitle}</h1>
    </>
  );
};
