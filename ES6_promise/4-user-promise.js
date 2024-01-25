// Simple promise

export default function signUpUser(firstName, lastName) {
  return new Promise((resolve) => {
    const result = {
      firstName,
      lastName,
    };
    resolve(result);
  });
}
