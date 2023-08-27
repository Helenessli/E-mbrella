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
        <form class="form" method="post">
            <label for="user_input">Enter a sentence: </label>
            <input type="text" name="user_input">
            <button type="submit" name="submit">Submit</button>
        </form>
        <div class="result">
            <?php
            if ($_SERVER["REQUEST_METHOD"] == "POST") {
                $user_input = $_POST["user_input"];
                $output = shell_exec("python text.py $user_input");
                $prediction = $output[1];
                $confidence_score = substr($output, 3, 5);
                if ($prediction == 1) {
                    if ($confidence_score >= 0.6){
                        $pred_result = "Predator";
                        $text_color = "red";
                    }else{$pred_result = "Might be a Predator"; $text_color = "orange";}
                } else {
                    $pred_result = "Normal";
                    $text_color = "green";
                }
                echo "<p> Message: $user_input </p>";
                echo "<p style='color: $text_color;'> Result: $pred_result </p>";
                echo "<p> Confidence level: $confidence_score </p>";

                echo '<button type="button" id="flagButton">Flag</button>';
                echo '<div id="flagTextBox" style="display: none;">';
                echo '<textarea name="flagReason" placeholder="Enter flag reason"></textarea>';
                echo '<button type="button" id="submitFlagButton">Submit Flag</button>';
                echo '</div>';
            }

            
            ?>
        </form>
        </div>
    </div>

    <script>
        // JavaScript to show/hide the flag text box
        document.getElementById("flagButton").addEventListener("click", function () {
            var flagTextBox = document.getElementById("flagTextBox");
            flagTextBox.style.display = flagTextBox.style.display === "none" ? "block" : "none";
        });

        // Add any additional JavaScript code here for handling flag submission
        // For example, you can use AJAX to send the flag reason to the server.
    </script>

</body>

</html>