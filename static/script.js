document.getElementById("predictForm").addEventListener("submit", async function(e){

    e.preventDefault();

    let formData = new FormData(this);

    let response = await fetch("/predict", {
        method: "POST",
        body: formData
    });

    let data = await response.json();

    document.getElementById("result").innerHTML =
        "Result: " + data.prediction;

});
