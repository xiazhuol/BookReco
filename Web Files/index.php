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
        <a class="navbar-brand" href="#">Music Artist Recomendations</a>
      </div>
      <div class="collapse navbar-collapse" id="myNavbar">
      </div>
    </div>
  </nav>

  <div class="container-fluid text-center">
    <div class="row content">

      <div class="col-sm-8 text-left">
        <form action ="signIn.php" method = "POST">
          <p> Enter User ID: </p> <input type = "text" name ="u_id"><br/><br/>
          <p> Enter Password: </p> <input type = "password" name ="pw"><br/>
        <input type = "submit" name = "submit" value="Submit">
        </form>
        
        <?php
			if (isset($_GET["msg"]) && $_GET["msg"] == 'failed') {
			echo "Wrong Username / Password. Please Try Again!";
			}

		?>
<br/><br/>
      </div>

	

    </div>
  </div>
	
  <footer class="container-fluid text-center">
    <p>CSE 482</p>
  </footer>


</body>

</html>




