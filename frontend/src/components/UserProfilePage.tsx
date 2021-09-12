import React from "react";
import { useParams } from "react-router";
import { debounce } from "lodash";
import profile from "../services/profile";
import TextComponent from "../components/controls/TextComponent";
import { IUserInStorage, IUserProfile } from "../types";
import getUser from "../services/getUser";
import { Avatar, makeStyles } from "@material-ui/core";

const useStyles = makeStyles((theme) => ({
  mainWrapper: {
    display: "flex",
    flexDirection: "column",
    textAlign: "center",
    justifyContent: "center",
    alignItems: "center",
  },
  avatar: {
    height: "150px",
    width: "150px",
    borderRadius: theme.spacing(1),
  },
}));

interface IRouteParams {
  targetUsername: string;
}

export const UserProfilePage: React.FC = () => {
  let { targetUsername } = useParams<IRouteParams>();
  const classes = useStyles();
  const [userProfile, setUserProfile] = React.useState<IUserProfile>(null);
  const [editable, setEditable] = React.useState<boolean>(false);
  const [currentUser, setCurrentUser] = React.useState<IUserInStorage>(null);

  const [firstName, setFirstName] = React.useState<string>(null);
  const [lastName, setLastName] = React.useState<string>(null);
  const [bio, setBio] = React.useState<string>(null);
  const [avatar, setAvatar] = React.useState<string>(null);

  React.useEffect(() => {
    setCurrentUser(getUser());
  }, []);

  React.useEffect(() => {
    if (targetUsername !== undefined) {
      profile.getProfile(targetUsername).then((pro) => {
        setUserProfile(pro);
      });
    }
    if (currentUser !== null && currentUser.username === targetUsername) {
      setEditable(true);
      console.log("editable: ", editable);
    }
  }, [currentUser, targetUsername]);

  const updateProfileDebounced = debounce(() => {
    console.log(userProfile);
    if (userProfile !== null) {
      if (
        userProfile.first_name !== firstName ||
        userProfile.last_name !== lastName ||
        userProfile.bio !== bio ||
        userProfile.avatar !== avatar
      ) {
        profile.updateProfile({
          username: userProfile.username,
          first_name: firstName,
          last_name: lastName,
          bio,
          avatar,
        });
        profile.updateCachedProfile(userProfile.username);
      }
    }
  }, 1000);

  React.useEffect(() => {
    console.log("changed: ", firstName, lastName, bio, avatar);
    updateProfileDebounced();
  }, [firstName, lastName, bio, avatar]);

  React.useEffect(() => {
    if (userProfile !== null) {
      setFirstName(userProfile.first_name);
      setLastName(userProfile.last_name);
      setBio(userProfile.bio);
      setAvatar(userProfile.avatar);
    }
  }, [userProfile]);

  return (
    <div>
      {userProfile === null ? (
        <p>No profile!</p>
      ) : (
        <div className={classes.mainWrapper}>
          <Avatar
            alt={`${userProfile.last_name}, ${userProfile.first_name}`}
            src={avatar}
            className={classes.avatar}
          />
          <h2>{userProfile.username}</h2>
          <TextComponent
            value={firstName}
            setValue={setFirstName}
            editable={editable}
            label="First Name"
          />
          <TextComponent
            value={lastName}
            setValue={setLastName}
            editable={editable}
            label="Last Name"
          />
          <TextComponent
            value={bio}
            setValue={setBio}
            editable={editable}
            label="Biography"
            multiline={true}
          />
          {editable && (
            <TextComponent
              value={avatar}
              setValue={setAvatar}
              editable={editable}
              label="Avatar"
            />
          )}
        </div>
      )}
    </div>
  );
};
