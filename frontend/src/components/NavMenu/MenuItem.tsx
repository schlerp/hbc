import * as React from "react";
import { motion } from "framer-motion";
import { makeStyles } from "@material-ui/core";
import { Link } from "react-router-dom";

const useStyles = makeStyles((theme) => ({
  li: {
    margin: 0,
    padding: 0,
    listStyle: "none",
    marginBottom: "20px",
    display: "flex",
    alignItems: "center",
    cursor: "pointer",
  },
}));

const variants = {
  open: {
    y: 0,
    opacity: 1,
    transition: {
      y: { stiffness: 1000, velocity: -200 },
    },
  },
  closed: {
    y: 50,
    opacity: 0,
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
    <Link to={href}>
      <motion.li
        variants={variants}
        whileHover={{ scale: 1.05 }}
        whileTap={{ scale: 0.95 }}
        className={classes.li}
        onClick={handleClick}
      >
        {text}
      </motion.li>
    </Link>
  );
};
