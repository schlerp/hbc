import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import { motion } from "framer-motion";

const useStyles = makeStyles((theme) => ({
  button: {
    width: "150px",
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
}

export const Button: React.FC<ButtonIface> = ({ label = "" }) => {
  const classes = useStyles();
  return (
    <motion.button
      className={classes.button}
      whileHover={{ scale: 1.05 }}
      whileTap={{ scale: 0.95 }}
    >
      {label}
    </motion.button>
  );
};

export default Button;
