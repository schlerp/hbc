import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import { motion } from "framer-motion";

const useStyles = makeStyles((theme) => ({
  button: {
    width: "100px",
    height: "50px",
    background: theme.palette.secondary.main,
    color: theme.palette.secondary.contrastText,
    borderRadius: "5px",
    borderWidth: "0px",
    boxShadow: theme.shadows[1],
  },
}));

interface ButtonIface {
  label: string;
  className?: any;
}

export const Button: React.FC<ButtonIface> = ({ label = "", className }) => {
  const classes = useStyles();
  return (
    <motion.button
      className={`${classes.button} ${className}`}
      whileHover={{ scale: 1.01 }}
      whileTap={{ scale: 0.99 }}
    >
      {label}
    </motion.button>
  );
};

export default Button;
