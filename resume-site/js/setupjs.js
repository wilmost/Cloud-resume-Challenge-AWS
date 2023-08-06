
fetch('https://2sjnb63exh.execute-api.us-east-1.amazonaws.com/Prod/update-web-visit')
    .then(response => response.json())
    .then((data) => {
        document.getElementById('counter').innerText = data.visitors
    })