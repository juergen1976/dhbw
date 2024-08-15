<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Guestbook</title>
</head>
<body>
    <h1>Guestbook</h1>
    <form method="POST">
        <input type="text" name="name" placeholder="Ihr Name" required><br>
        <textarea name="message" placeholder="Ihre Nachricht" required></textarea><br>
        <button type="submit">Submit</button>
    </form>
    
    <?php
        $file = "guestbook.txt";
        // Check if the form was submitted
        if ($_SERVER['REQUEST_METHOD'] == 'POST') {
            $entry = htmlspecialchars($_POST['name']) . ": " . ($_POST['message']) . "\n";

            // Attempt to write to the file and check for errors
            if (file_put_contents($file, $entry, FILE_APPEND | LOCK_EX) === false) {
                echo "<p>Error writing to guestbook.txt. Please check file permissions.</p>";
            }
        }
        // Check if the file exists and is readable
        if (file_exists($file) && is_readable($file)) {
            $entries = file_get_contents($file);
            echo nl2br($entries);
        } else {
            echo "<p>No entries yet, or unable to read guestbook.txt.</p>";
        }
    ?>
</body>
</html>
