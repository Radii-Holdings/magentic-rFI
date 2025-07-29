import React from "react";
import LoginForm from "../components/LoginForm";

const LoginPage: React.FC = () => {
  return (
    <div className="flex items-center justify-center h-screen bg-primary">
      <LoginForm />
    </div>
  );
};

export default LoginPage;
