import { db } from "./firebase.js";

import {
collection,
getDocs,
doc,
updateDoc,
deleteDoc
} from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";

const table = document.getElementById("adminTable");

const totalReports = document.getElementById("totalReports");
const pendingReports = document.getElementById("pendingReports");
const resolvedReports = document.getElementById("resolvedReports");

async function loadReports(){

table.innerHTML="";

const snapshot = await getDocs(collection(db,"reports"));

let total=0;
let pending=0;
let resolved=0;

snapshot.forEach((report)=>{

const data = report.data();

total++;

if(data.status==="Resolved"){
resolved++;
}else{
pending++;
}

const row=document.createElement("tr");

row.innerHTML=`

<td>${data.name}</td>

<td>${data.issueType}</td>

<td>${data.location}</td>

<td>${data.status || "Pending"}</td>

<td>

<button class="resolve"
onclick="resolveReport('${report.id}')">

Resolve

</button>

<button class="delete"
onclick="deleteReport('${report.id}')">

Delete

</button>

</td>

`;

table.appendChild(row);

});

totalReports.innerHTML=total;
pendingReports.innerHTML=pending;
resolvedReports.innerHTML=resolved;

}

window.resolveReport=async(id)=>{

await updateDoc(doc(db,"reports",id),{

status:"Resolved"

});

alert("Report Marked as Resolved");

location.reload();

}

window.deleteReport=async(id)=>{

if(confirm("Delete this report?")){

await deleteDoc(doc(db,"reports",id));

alert("Report Deleted");

location.reload();

}

}

loadReports();