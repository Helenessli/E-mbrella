<!DOCTYPE html>
<html>
<head>
    <title>Predator Detector</title>
    <link rel="stylesheet" type="text/css" href="app.css">
</head>
<body>
    <div class="container">
        <h1>E-mbrella Predator Detector</h1>
        <form method="post">
            <label for="user_input">Enter a sentence:</label>
            <input type="text" name="user_input">
            <button type="submit">Submit</button>
        </form>
        <div class="result">
            <?php
            if ($_SERVER["REQUEST_METHOD"] == "POST") {
                $user_input = $_POST["user_input"];
                $output = shell_exec("python text.py $user_input");
                $prediction = $output[1];
                $confidence_score = substr($output, 3, 7);
                if ($prediction == 1){
                    $pred_result = "Predator";
                }else{$pred_result = "Normal";}
                echo "<p>Result: $pred_result</p>";
                echo "<p>Confidence level: $confidence_score</p>";
            }
            ?>
        </div>
    </div>
</body>
</html>
