import '@testing-library/jest-dom/extend-expect';
import { fireEvent } from '@testing-library/dom';
import fetchMock from 'jest-fetch-mock';

fetchMock.enableMocks();

beforeEach(() => {
  fetchMock.resetMocks();
  document.body.innerHTML = `
    <form id="login-form">
      <input name="email" type="email" value="test@example.com" />
      <input name="password" type="password" value="password123" />
      <button type="submit">Login</button>
    </form>
    <form id="signup-form">
      <input name="email" type="email" value="test@example.com" />
      <input name="password" type="password" value="password123" />
      <button type="submit">Sign Up</button>
    </form>
  `;
  require('./scripts'); // Ensure the script is loaded
});

test('loginUser function', async () => {
  fetchMock.mockResponseOnce(JSON.stringify({ message: 'Connexion réussie' }));

  const loginForm = document.getElementById('login-form');
  fireEvent.submit(loginForm);

  expect(fetchMock).toHaveBeenCalledWith('https://your-api-url/login', expect.any(Object));
  expect(fetchMock).toHaveBeenCalledTimes(1);
});

test('registerUser function', async () => {
  fetchMock.mockResponseOnce(JSON.stringify({ message: 'Inscription réussie' }));

  const signupForm = document.getElementById('signup-form');
  fireEvent.submit(signupForm);

  expect(fetchMock).toHaveBeenCalledWith('https://your-api-url/register', expect.any(Object));
  expect(fetchMock).toHaveBeenCalledTimes(1);
});
