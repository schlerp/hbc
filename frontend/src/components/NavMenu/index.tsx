import * as React from "react";
import { useRef } from "react";
import { makeStyles } from "@material-ui/core";
import { motion, useCycle } from "framer-motion";
import { useDimensions } from "../../hooks/useDimensions";
import { MenuToggle } from "./MenuToggle";
import { Navigation } from "./Navigation";
import { IUserInStorage } from "../../types";
// import { Button } from "../controls/Button";

const sidebar = {
  open: (height = 1000) => ({
    clipPath: `circle(${height * 2 + 200}px at 40px 40px)`,
    transition: {
      type: "spring",
      stiffness: 20,
      restDelta: 2,
    },
  }),
  closed: {
    clipPath: "circle(30px at 40px 40px)",
    transition: {
      delay: 0.1,
      type: "spring",
      stiffness: 400,
      damping: 40,
    },
  },
};

const useStyles = makeStyles((theme) => ({
  nav: {
    position: "absolute",
    top: 0,
    left: 0,
    bottom: 0,
    width: "200px",
    zIndex: 11,
  },
  background: {
    position: "absolute",
    top: 0,
    left: 0,
    bottom: 0,
    width: "200px",
    background: theme.palette.secondary.main,
    boxShadow: "0px 1px 3px 3px rgba(0,0,0,0.12)",
    zIndex: 10,
  },
}));

interface INavMenuProps {
  currentUser: IUserInStorage;
}

export const NavMenu: React.FC<INavMenuProps> = ({ currentUser }) => {
  const classes = useStyles();
  const [isOpen, toggleOpen] = useCycle(false, true);
  const containerRef = useRef(null);
  const { height } = useDimensions(containerRef);

  return (
    <motion.nav
      initial={false}
      animate={isOpen ? "open" : "closed"}
      custom={height}
      ref={containerRef}
      className={classes.nav}
    >
      <motion.div className={classes.background} variants={sidebar} />
      <Navigation toggle={() => toggleOpen()} currentUser={currentUser} />
      <MenuToggle toggle={() => toggleOpen()} />
    </motion.nav>
  );
};

export default NavMenu;
