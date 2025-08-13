document.getElementById("predictForm").addEventListener("submit", function(e) {
    e.preventDefault();

    const feature1 = parseFloat(document.getElementById("feature1").value);
    const feature2 = parseFloat(document.getElementById("feature2").value);
    const feature3 = parseFloat(document.getElementById("feature3").value);

    fetch("http://127.0.0.1:5000/predict", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ features: [feature1, feature2, feature3] })
    })
        .then(response => response.json())
        .then(data => {
            document.getElementById("result").textContent = "Calories burned: " + data.calories_burned;
        });
});
