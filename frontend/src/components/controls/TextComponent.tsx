import { makeStyles, TextField } from "@material-ui/core";
import React from "react";

const useStyles = makeStyles((theme) => ({
  text: {
    margin: theme.spacing(1),
  },
}));

interface ITextComponentProps {
  editable: boolean;
  value: string;
  setValue?: Function;
  label?: string;
  multiline?: boolean;
}

export const TextComponent: React.FC<ITextComponentProps> = ({
  editable,
  value,
  setValue,
  label,
  multiline = false,
}) => {
  const classes = useStyles();
  if (editable) {
    return (
      <TextField
        label={label}
        value={value}
        onChange={(e) => {
          setValue(e.target.value);
        }}
        variant="outlined"
        className={classes.text}
        multiline={multiline}
      />
    );
  }
  return <p>{value}</p>;
};

export default TextComponent;
