// import React, { useState } from 'react';
// import './Signup.css';
// import { useNavigate } from 'react-router-dom';
// // import { registerUser } from '../../api';

// export default function Signup() {
//     const [username, setUsername] = useState('');
//     const [email, setEmail] = useState('');
//     const [password, setPassword] = useState('');
//     const navigate = useNavigate();

//     const handleSubmit = async (e) => {
//         e.preventDefault();
//         try {
//             const data = await registerUser(username, email, password);
//             localStorage.setItem('token', data.token);
//             navigate('/');
//         } catch (error) {
//             console.error('Signup failed', error);
//         }
//     };

//     return (
//         <form onSubmit={handleSubmit}>
//             <input
//                 type='text'
//                 value={username}
//                 onChange={(e) => setUsername(e.target.value)}
//                 placeholder='Username'
//                 required
//             />
//             <input
//                 type='email'
//                 value={email}
//                 onChange={(e) => setEmail(e.target.value)}
//                 placeholder='Email'
//                 required
//             />
//             <input
//                 type='password'
//                 value={password}
//                 onChange={(e) => setPassword(e.target.value)}
//                 placeholder='Password'
//                 required
//             />
//             <button type='submit'>Signup</button>
//         </form>
//     );
// }
