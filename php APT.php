<?php

$full_name = $_POST['full_name'];
$email = $_POST['email'];
$username = $_POST['username'];
$password = $_POST['password'];


$hashed_password = password_hash($password, PASSWORD_DEFAULT);

// Database connection details
$servername = "local_host";
$username_db = "user_id";
$password_db = "password";
$dbname = "Konnectus";

// Create connection
$conn = new mysqli($servername, $username_db, $password_db, $dbname);

// Check connection
if ($conn->connect_error) {
    die("Connection failed: " . $conn->connect_error);
}

// Insert data into the 'users' table
$sql = "INSERT INTO users (full_name, email, username, password) 
        VALUES ('$full_name', '$email', '$username', '$hashed_password')";

if ($conn->query($sql) === TRUE) {
    echo "User registered successfully";
} else {
    echo "Error: " . $sql . "<br>" . $conn->error;
}

$conn->close();
?>
