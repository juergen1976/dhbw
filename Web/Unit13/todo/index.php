<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>To-Do List</title>
</head>
<body>
    <h1>To-Do List</h1>
    <form method="POST">
        <input type="text" name="task" placeholder="Enter a new task">
        <button type="submit">Add Task</button>
    </form>

<?php
    session_start();

    if (!isset($_SESSION['tasks'])) {
        $_SESSION['tasks'] = [];
    }

    if ($_SERVER['REQUEST_METHOD'] == 'POST' && !empty($_POST['task'])) {
        $_SESSION['tasks'][] = htmlspecialchars($_POST['task']);
    }

    $tasks = $_SESSION['tasks'];
?>
<ul>
    <?php foreach ($tasks as $task): ?>
        <li><?php echo $task; ?></li>
    <?php endforeach; ?>
</ul>

