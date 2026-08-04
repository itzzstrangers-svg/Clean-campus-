// Firebase SDK

import { initializeApp } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-app.js";

import { getFirestore } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-firestore.js";

import { getStorage } from "https://www.gstatic.com/firebasejs/10.12.2/firebase-storage.js";

// Firebase Configuration

const firebaseConfig = {

apiKey: "AIzaSyAGmK7sS8cJo8CKYtuauvJa-0JfxRul010",

authDomain: "clean-campus-reporting.firebaseapp.com",

projectId: "clean-campus-reporting",

storageBucket: "clean-campus-reporting.firebasestorage.app",

messagingSenderId: "839839694169",

appId: "1:839839694169:web:0f995966f8c07dd7806048",

measurementId: "G-81VVPHT7XZ"

};

// Initialize Firebase

const app = initializeApp(firebaseConfig);

// Firestore Database

const db = getFirestore(app);

// Firebase Storage

const storage = getStorage(app);

// Export

export { db, storage };