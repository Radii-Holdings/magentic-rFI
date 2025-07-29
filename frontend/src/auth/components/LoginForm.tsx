import React, { useState, useContext } from "react";
import { Input } from "antd";
import { Button } from "../../components/common/Button";
import { appContext } from "../../hooks/provider";
import { navigate } from "gatsby";

const LoginForm: React.FC = () => {
  const { setUser } = useContext(appContext);
  const [username, setUsername] = useState("");
  const [password, setPassword] = useState("");

  const handleLogin = async () => {
    const body = new URLSearchParams({ username, password });
    const resp = await fetch("/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/x-www-form-urlencoded" },
      body: body.toString(),
    });
    if (resp.ok) {
      setUser({ name: username, email: username });
      navigate("/");
    } else {
      alert("Invalid credentials");
    }
  };

  return (
    <div className="p-4 border rounded w-80 bg-primary text-primary">
      <h1 className="text-xl mb-4">Login</h1>
      <Input
        placeholder="Username"
        value={username}
        onChange={(e) => setUsername(e.target.value)}
        className="mb-2"
      />
      <Input.Password
        placeholder="Password"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        className="mb-4"
      />
      <Button onClick={handleLogin} fullWidth>
        Login
      </Button>
    </div>
  );
};

export default LoginForm;
