// src/services/api.js

export const registerUser = async (username, email, password) => {
    const response = await fetch('/api/signup', { // Update the URL to your backend endpoint
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify({ username, email, password }),
    });

    if (!response.ok) {
        throw new Error('Failed to register');
    }

    return await response.json(); // Assumes your API returns a JSON response
};
