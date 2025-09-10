import axios from "axios";

const BASE_URL = "http://127.0.0.1:8000"; // change to your backend URL

export const getResults = async () => {
  const res = await axios.get(`${BASE_URL}/results`);
  return res.data; // returns results dictionary
};
