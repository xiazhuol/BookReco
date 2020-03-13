<!DOCTYPE html>
<html lang="en">

<head>
  <title>Music Artist Recomendation</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.2.1/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/js/bootstrap.min.js"></script>
  <style>
  	.navbar{
  	  background-color: #18453b;
      font: white;
      border: 0;
      
  	}

	.navbar-li{ 
	  color:white
	}

    footer {
      background-color: #18453b;
      color: white;
      padding: 15px;
    }
  
  </style>
</head>

<body>


 <nav class="navbar navbar-inverse">
    <div class="container-fluid">
      <div class="navbar-header">
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
          <span class="icon-bar"></span>
        </button>
        <a class="navbar-brand" href="index.php">Music Artist Recomendations</a>
      </div>
      <div class="collapse navbar-collapse" id="myNavbar">
      </div>
    </div>
  </nav>
  
  <h3>Welcome User</h3>
  
<?php
include 'validation.php';
error_reporting(E_ALL);
ini_set('display_errors', 'on');
$id =$_SESSION['username'];

$link = mysqli_connect("mysql-user.cse.msu.edu", "kolisett", "A46610134");
mysqli_select_db($link, "kolisett");

$sql = "SELECT name, userID, artistRec1, artistRec2, artistRec3 FROM ArtistRecommendation WHERE userID='$id'";
$disp = mysqli_query($link, $sql);


while($result = mysqli_fetch_assoc($disp))
{
	echo "<br/> Name: " . $result['name'];
	echo "<br>";
	echo "<br/> Artist Recomendation 1: " . $result['artistRec1'];
	echo "<br/> Artist Recomendation 2: " . $result['artistRec2'];
	echo "<br/> Artist Recomendation 3: " . $result['artistRec3'];
	echo "<br>";	
}


?>

   <h1></h1>
   
    <form action = "index.php" method = "POST">
        <input type = "submit" name = "Logout" value="Logout">
     </form>
  <footer class="container-fluid text-center">
    <p>CSE 482</p>
  </footer>


</body>
