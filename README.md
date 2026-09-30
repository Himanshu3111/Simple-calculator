<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Simple Calculator README</title>
    <style>
        :root {
            --bg: #f4f7fb;
            --card: #ffffff;
            --primary: #2563eb;
            --primary-dark: #1d4ed8;
            --accent: #10b981;
            --text: #1f2937;
            --muted: #6b7280;
            --border: #e5e7eb;
            --shadow: 0 12px 30px rgba(37, 99, 235, 0.12);
        }

        * {
            box-sizing: border-box;
        }

        body {
            margin: 0;
            font-family: Arial, Helvetica, sans-serif;
            background: linear-gradient(135deg, #eef4ff 0%, #f8fafc 100%);
            color: var(--text);
            line-height: 1.6;
        }

        .container {
            max-width: 920px;
            margin: 40px auto;
            padding: 24px;
        }

        .card {
            background: var(--card);
            border: 1px solid var(--border);
            border-radius: 18px;
            box-shadow: var(--shadow);
            padding: 32px;
        }

        h1 {
            margin-top: 0;
            font-size: 2.4rem;
            color: var(--primary-dark);
        }

        .badge {
            display: inline-block;
            background: rgba(37, 99, 235, 0.1);
            color: var(--primary-dark);
            padding: 8px 12px;
            border-radius: 999px;
            font-size: 0.85rem;
            font-weight: bold;
            margin-bottom: 18px;
        }

        p {
            margin: 0 0 16px;
            color: var(--text);
        }

        ul,
        ol {
            margin: 0 0 20px 20px;
            padding-left: 16px;
        }

        li {
            margin-bottom: 8px;
        }

        .operations {
            display: grid;
            grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
            gap: 12px;
            margin: 22px 0;
        }

        .operation {
            background: #f8fafc;
            border: 1px solid var(--border);
            border-radius: 12px;
            padding: 14px 16px;
            font-weight: 600;
            color: var(--text);
        }

        .code-box {
            background: #0f172a;
            color: #e2e8f0;
            padding: 18px;
            border-radius: 12px;
            overflow-x: auto;
            font-family: "Courier New", Courier, monospace;
            font-size: 0.95rem;
            margin: 18px 0;
        }

        .footer {
            margin-top: 26px;
            padding-top: 18px;
            border-top: 1px solid var(--border);
            color: var(--muted);
            font-size: 0.96rem;
        }
    </style>
</head>

<body>
    <div class="container">
        <div class="card">
            <div class="badge">Python Project</div>
            <h1>Simple Calculator</h1>

            <p>
                This project is a basic calculator written in Python. It performs common arithmetic
                operations and is designed for learning and practice.
            </p>

            <h2>Features</h2>
            <ul>
                <li>Addition</li>
                <li>Subtraction</li>
                <li>Multiplication</li>
                <li>Division</li>
                <li>Average</li>
                <li>Square</li>
                <li>Cube</li>
                <li>Square Root</li>
                <li>Cube Root</li>
            </ul>

            <h2>Available Operations</h2>
            <div class="operations">
                <div class="operation">1. Addition</div>
                <div class="operation">2. Subtraction</div>
                <div class="operation">3. Multiplication</div>
                <div class="operation">4. Division</div>
                <div class="operation">5. Average</div>
                <div class="operation">6. Square</div>
                <div class="operation">7. Cube</div>
                <div class="operation">8. Square Root</div>
                <div class="operation">9. Cube Root</div>
            </div>

            <h2>How to Run</h2>
            <p>Open the project folder and run the Python script in the terminal:</p>

            <div class="code-box">python calculator.py</div>

            <h2>Example</h2>
            <p>When the program starts, it displays a menu and asks the user to choose an operation.</p>

            <div class="code-box">
                Select a operator from 1, 2, 3, 4, 5, 6, 7, 8 or 9: 1
                Enter first number: 10
                Enter second number: 5
                10 + 5 = 15
            </div>

            <div class="footer">
                Created for simple arithmetic practice and beginner Python learning.
            </div>
        </div>
    </div>
</body>

</html>