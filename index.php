<!DOCTYPE html>
<html>

<head>
    <title>Predator Detector</title>
    <link rel="stylesheet" type="text/css" href="app.css">
</head>

<body>
    <div class="header">
        <h1 class="h1">E-mbrella Predator Detector</h1>
    </div>
    <div class="body">
        <div class="formcontainer">
        <form class="form" method="post">
            <label for="user_input" class="label">Enter a message:</label><br>
            <input type="text" name="user_input"><br>
            <button type="submit">Submit</button>
        </form>
        </div>
        <div class="result">
            <?php
            if ($_SERVER["REQUEST_METHOD"] == "POST") {
                $user_input = $_POST["user_input"];
                $output = shell_exec("python text.py $user_input");
                $prediction = $output[1];
                $confidence_score = substr($output, 3, 7);
                $resultStyle = ""; // Initialize style variable

                if ($prediction == 1) {
                    if ($confidence_score > 0.60) {
                        $resultStyle = "color: red;";
                    } else {
                        $resultStyle = "color: orange;";
                    }
                    $pred_result = "Predator";
                } else {
                    $resultStyle = "color: green;";
                    $pred_result = "Normal";
                }
            
                echo "<p class=\"message\">Message: $user_input</p>";
                echo "<p class=\"result\" style=\"$resultStyle\">Result: $pred_result</p>";
                echo "<p class=\"confidence\">Confidence level: $confidence_score</p>";
            
            }
            ?>
        </div>
    </div>

</body>

</html>