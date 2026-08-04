import { db } from "./firebase.js";

import {
collection,
getDocs
} from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";

const reportsContainer = document.getElementById("reportsContainer");

async function loadReports(){

reportsContainer.innerHTML="Loading Reports...";

const querySnapshot = await getDocs(collection(db,"reports"));

reportsContainer.innerHTML="";

querySnapshot.forEach((doc)=>{

const data = doc.data();

reportsContainer.innerHTML += `

<div class="report-card">

<h3>${data.issueType}</h3>

<p><b>Name:</b> ${data.name}</p>

<p><b>Email:</b> ${data.email}</p>

<p><b>Department:</b> ${data.department}</p>

<p><b>Location:</b> ${data.location}</p>

<p><b>Description:</b> ${data.description}</p>

<p><b>Status:</b> ${data.status}</p>

<p><b>Date:</b> ${data.date}</p>

</div>

`;

});

}

loadReports();