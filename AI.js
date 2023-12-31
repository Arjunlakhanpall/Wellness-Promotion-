const axios = require('axios');

const apiKey = 'YOUR_API_KEY';
const apiUrl = 'https://api.openai.com/v1/engines/text-davinci-003/completions'; // Update the engine version if needed

const prompt = 'Generate a JavaScript function to add two numbers:';

axios.post(apiUrl, {
  prompt,
  max_tokens: 100,
}, {
  headers: {
    'Content-Type': 'application/json',
    'Authorization': `Bearer ${apiKey}`,
  },
})
.then(response => {
  const generatedCode = response.data.choices[0].text;
  console.log(generatedCode);
})
.catch(error => console.error(error));
