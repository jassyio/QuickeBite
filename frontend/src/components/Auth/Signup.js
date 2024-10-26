// import React, { useState } from 'react';
// import './Signup.css'; // Import the CSS file for styling
// import { useNavigate, Link } from 'react-router-dom'; // Import Link for navigation
// import { registerUser } from '../../services/api'; // Ensure this path is correct

// export default function Signup() {
//     const [username, setUsername] = useState('');
//     const [email, setEmail] = useState('');
//     const [password, setPassword] = useState('');
//     const [error, setError] = useState(''); // State to handle error messages
//     const navigate = useNavigate();

//     const handleSubmit = async (e) => {
//         e.preventDefault();
//         try {
//             const data = await registerUser(username, email, password);
//             localStorage.setItem('token', data.token);
//             navigate('/'); // Redirect to homepage or desired route after signup
//         } catch (error) {
//             setError('Signup failed. Please try again.'); // Update error state
//             console.error('Signup failed:', error);
//         }
//     };

//     return (
//         <div className="signup-container">
//             <form onSubmit={handleSubmit} className="signup-form">
//                 <h2>Create Your Account</h2>
//                 <p>Sign up to start enjoying delicious meals.</p>
//                 {error && <p className="error-message">{error}</p>} {/* Display error message if exists */}
//                 <input
//                     type="text"
//                     value={username}
//                     onChange={(e) => setUsername(e.target.value)}
//                     placeholder="Username"
//                     required
//                 />
//                 <input
//                     type="email"
//                     value={email}
//                     onChange={(e) => setEmail(e.target.value)}
//                     placeholder="Email"
//                     required
//                 />
//                 <input
//                     type="password"
//                     value={password}
//                     onChange={(e) => setPassword(e.target.value)}
//                     placeholder="Password"
//                     required
//                 />
//                 <button type="submit">Sign Up</button>
//                 <p>Already have an account? <Link to="/login">Log In</Link></p> {/* Link to login */}
//             </form>
//         </div>
//     );
// }
