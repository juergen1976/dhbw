<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Gästebuch von Jürgen - Bitte nur nette Nachrichten</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>

<body class="bg-gray-100 flex items-center justify-center min-h-screen">

    <div class="bg-white shadow-md rounded-lg p-6 max-w-md w-full">
        <h1 class="text-2xl font-bold text-center text-gray-800 mb-6">Gästebuch von Jürgen - Bitte nur nette Nachrichten</h1>
        <form method="POST" class="space-y-4">
            <div>
                <input type="text" name="name" placeholder="Your Name" required
                    class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500">
            </div>
            <div>
                <textarea name="message" placeholder="Your Message" required
                    class="w-full px-4 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-blue-500 h-32"></textarea>
            </div>
            <button type="submit"
                class="w-full bg-blue-500 text-white font-bold py-2 px-4 rounded-md hover:bg-blue-600 transition duration-300">
                Submit
            </button>
        </form>

        <div class="mt-8">
            <?php
            $file = "guestbook.txt";
            // Check if the form was submitted
            if ($_SERVER['REQUEST_METHOD'] == 'POST') {
                $entry = htmlspecialchars($_POST['name']) . ": " . htmlspecialchars($_POST['message']) . "\n";

                // Attempt to write to the file and check for errors
                if (file_put_contents($file, $entry, FILE_APPEND | LOCK_EX) === false) {
                    echo "<p class='text-red-500'>Error writing to guestbook.txt. Please check file permissions.</p>";
                }
            }

            // Check if the file exists and is readable
            if (file_exists($file) && is_readable($file)) {
                $entries = file_get_contents($file);
                echo "<div class='mt-4 p-4 bg-gray-50 rounded-md'><p>" . nl2br($entries) . "</p></div>";
            } else {
                echo "<p class='text-gray-500 mt-4'>No entries yet, or unable to read guestbook.txt.</p>";
            }
            ?>
        </div>
    </div>

</body>

</html>