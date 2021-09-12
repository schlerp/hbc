import * as React from "react";
import { motion } from "framer-motion";
import { makeStyles } from "@material-ui/core";
import { Link } from "react-router-dom";

const useStyles = makeStyles((theme) => ({
  li: {
    margin: 0,
    padding: theme.spacing(1),
    borderRadius: theme.spacing(1),
    listStyle: "none",
    marginBottom: "20px",
    display: "flex",
    alignItems: "center",
    cursor: "pointer",
    background: theme.palette.primary.main,
  },
  text: {
    textDecoration: "none",
    color: theme.palette.primary.contrastText,
    textAlign: "center",
  },
}));

const variants = {
  open: {
    y: 0,
    opacity: 1,
    display: "",
    transition: {
      y: { stiffness: 1000, velocity: -200 },
    },
  },
  closed: {
    y: 50,
    opacity: 0,
    display: "none",
    transition: {
      y: { stiffness: 1000 },
    },
  },
};

interface MenuItemIface {
  text: string;
  href?: string;
  toggle?: Function;
}

export const MenuItem: React.FC<MenuItemIface> = ({
  text,
  href = "#",
  toggle,
}) => {
  const classes = useStyles();
  const handleClick = () => {
    toggle();
  };
  return (
    <Link to={href} className={classes.text}>
      <motion.li
        variants={variants}
        whileHover={{ scale: 1.02 }}
        whileTap={{ scale: 0.98 }}
        className={classes.li}
        onClick={handleClick}
      >
        {text}
      </motion.li>
    </Link>
  );
};
