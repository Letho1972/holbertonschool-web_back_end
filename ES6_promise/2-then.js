// Append three handlers to the function.

export default function handleResponseFromAPI(promise) {
  return promise
    .then((response) => {
      console.log('Got a response from the API');
      return {
        status: 200,
        body: 'success',
      };
    })
    .catch((error) => {
      console.error('API request failed:', error);
      return new Error();
    });
}