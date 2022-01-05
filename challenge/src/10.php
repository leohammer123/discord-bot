<?php 
    
    if(isset($_GET["file"])){
        if($_GET["file"]=="index"){
            echo "<h1>Hellow there is the index page</h1><!---<a href='https://challenge1002.000webhostapp.com/c10/index.php?file=secret.php'>secret</a>!>";
        }
        else{
            $req = str_replace('/','',$_GET["file"]);
            $req .= ".php";
            echo file_get_contents($req);
        }
    }
    else{
        echo "<script>location.href = 'https://challenge1002.000webhostapp.com/c10/index.php?file=index.php'</script>";
    }

?>