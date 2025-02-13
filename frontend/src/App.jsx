import { GoogleOAuthProvider, GoogleLogin } from "@react-oauth/google";

const CLIENT_ID = import.meta.env.VITE_GOOGLE_CLIENT_ID;

function App() {
  const handleSuccess = async (response) => {
    // This is the id_token or authorization code from Google
    const googleAuthToken = response.credential;

    // Send the authorization code to your backend
    try {
      const res = await fetch(
        "http://localhost:8000/api/auth/google/callback/",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ token: googleAuthToken }), // Send the token to backend
        }
      );

      const data = await res.json();
      console.log("User Info: ", data); // Handle the user data (login or create user)
    } catch (error) {
      console.error("Error during Google authentication:", error);
    }
  };

  const handleFailure = (error) => {
    console.error("Google login failed:", error);
  };

  return (
    <GoogleOAuthProvider clientId={CLIENT_ID}>
      <div>
        <h1>Google Login</h1>
        <GoogleLogin
          onSuccess={handleSuccess}
          onError={handleFailure}
          clientId={CLIENT_ID} // Make sure the correct clientId is passed
        />
      </div>
    </GoogleOAuthProvider>
  );
}

export default App;
