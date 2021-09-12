import React from "react";
import { motion } from "framer-motion";
import { MenuItem } from "./MenuItem";
import { Avatar, makeStyles } from "@material-ui/core";
import { IUserInStorage } from "../../types";
import profile from "../../services/profile";

const useStyles = makeStyles((theme) => ({
  ul: {
    margin: 0,
    padding: "25px",
    position: "absolute",
    top: theme.spacing(6),
    width: "150px",
    zIndex: 20,
  },
  centered: {
    display: "flex",
    flexDirection: "column",
    alignItems: "center",
  },
  avatar: {
    width: "100px",
    height: "100px",
    borderRadius: theme.spacing(1),
  },
}));

const variants = {
  open: {
    transition: { staggerChildren: 0.07, delayChildren: 0.2 },
    display: "",
  },
  closed: {
    transition: { staggerChildren: 0.05, staggerDirection: -1 },
    display: "none",
  },
};

interface INavigationProps {
  toggle: Function;
  currentUser?: IUserInStorage;
}

export const Navigation: React.FC<INavigationProps> = ({
  toggle,
  currentUser = null,
}) => {
  const classes = useStyles();
  const [userProfile, setUserProfile] = React.useState(null);

  React.useEffect(() => {
    setUserProfile(profile.getLocalProfile());
  }, []);

  return (
    <motion.ul variants={variants} className={classes.ul}>
      {currentUser === null && (
        <>
          <MenuItem text="Sign up" href="/signup" toggle={toggle} />
          <MenuItem text="Log in" href="/signin" toggle={toggle} />
        </>
      )}

      {currentUser !== null && (
        <>
          <div className={classes.centered}>
            <Avatar
              alt={userProfile.username}
              src={userProfile.avatar}
              className={classes.avatar}
              variant="rounded"
            />
            <h2>{userProfile.username}</h2>
          </div>
          <MenuItem
            text={`My Profile`}
            href={`/profile/${currentUser.username}`}
            toggle={toggle}
          />
          <MenuItem text="My Entries" href="/entries" toggle={toggle} />
        </>
      )}

      <MenuItem text="Competitions" href="/comps" toggle={toggle} />

      {currentUser !== null && (
        <MenuItem text="Logout" href="/logout" toggle={toggle} />
      )}
    </motion.ul>
  );
};
