import { db } from "./firebase.js";

import {
collection,
addDoc
} from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";

const form = document.getElementById("reportForm");

form.addEventListener("submit", async (e) => {

e.preventDefault();

const report = {

name: document.getElementById("name").value,

email: document.getElementById("email").value,

department: document.getElementById("department").value,

issueType: document.getElementById("issueType").value,

location: document.getElementById("location").value,

description: document.getElementById("description").value,

date: new Date().toLocaleString(),

status: "Pending"

};

try{

await addDoc(collection(db,"reports"), report);

alert("✅ Report Submitted Successfully!");

form.reset();

}catch(error){

console.error(error);

alert("❌ Failed to submit report!");

}

});