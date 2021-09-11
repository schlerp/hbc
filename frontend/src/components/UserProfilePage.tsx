import React from "react";

interface IUserProfileProps {
  username: string;
}

export const UserProfile: React.FC<IUserProfileProps> = (props) => {
  return (
    <div>
      <p>hello: {props.username}</p>
    </div>
  );
};
