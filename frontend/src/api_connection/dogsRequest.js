// DjangoVueConnection/frontend/api_connection/dogsRequest.js

/* Get dogs data from the backend
*/

import axios from "axios";

export async function getDogs() {
  try {
    const response = await axios.get("api/dogs/");
    const dogs_data = response.data.results;
    return dogs_data;
  } catch (error) {
    console.error(error);
  }
}
