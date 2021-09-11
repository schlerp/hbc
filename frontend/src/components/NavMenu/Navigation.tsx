import * as React from "react";
import { motion } from "framer-motion";
import { MenuItem } from "./MenuItem";
import { makeStyles } from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
  ul: {
    margin: 0,
    padding: "25px",
    position: "absolute",
    top: "100px",
    width: "150px",
    zIndex: 20,
  },
}));

const variants = {
  open: {
    transition: { staggerChildren: 0.07, delayChildren: 0.2 },
  },
  closed: {
    transition: { staggerChildren: 0.05, staggerDirection: -1 },
  },
};

interface INavigationProps {
  toggle: Function;
}

export const Navigation: React.FC<INavigationProps> = ({ toggle }) => {
  const classes = useStyles();
  return (
    <motion.ul variants={variants} className={classes.ul}>
      <MenuItem text="Sign up" href="/signup" toggle={toggle} />
      <MenuItem text="Log in" href="/signin" toggle={toggle} />
    </motion.ul>
  );
};
