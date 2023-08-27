<!DOCTYPE html>
<html>
<head>
    <title>Predator Detector</title>
</head>
<body>
    <form method="post">
        <label for="user_input">Enter a word:</label>
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