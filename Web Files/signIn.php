<?php
  $id = $_POST['u_id'];
  $password = $_POST['pw'];

  // clear out any existing session that may exist
  session_start();
  session_destroy();
  session_start();

  if ($password==="cse482" && $id<616) {

    $_SESSION['signed_in'] = true;
    $_SESSION['username'] = $id;
    header("Location: display.php");
  } else {
    $_SESSION['signed_in'] = false;
    $_SESSION['username'] = null;
    header("location:index.php?msg=failed");
  }
?>
