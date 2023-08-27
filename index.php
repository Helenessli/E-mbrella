<!DOCTYPE html>
<html>
<head>
    <title>Predator Detector</title>
    <link rel="stylesheet" type="text/css" href="app.css">
</head>
<header class="header">
    <h1 class="h1">E-mbrella Detector</h1>
</header>
<body class="body">
    <form method="post">
        <label for="user_input">Enter a phrase:</label>
        <input type="text" name="user_input">
        <button type="submit">Submit</button>
    </form>
    <?php

    if ($_SERVER["REQUEST_METHOD"] == "POST") {
        $user_input = $_POST["user_input"];
        $output = shell_exec("python text.py $user_input");
        echo "<p>Result: $output</p>";
    }
    ?>
</body>
</html>