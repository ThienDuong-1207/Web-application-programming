document.getElementById("inputField").addEventListener("input",
(e) => {//arrow function revice e event to stored all info
    console.log(e.target.value);// e.target = id=inputFiled event + .value is value user input
});