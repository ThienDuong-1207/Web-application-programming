async function fetchUsers(){ // async function called fetchUsers
    try{
        // use fetch to send request http to APi, await = wait until return result
        const response = await fetch("https://jsonplaceholder.typicode.com/users"); 
        // Call .json() to convert the HTTP response to JSON format (JavaScript object).
        //users will be an array of user objects.
        const users = await response.json();

        const userList = document.getElementById("userList");
        users.forEach(user => {
            //create <li> tag, set innerText to the username(user.name)
            // append the <li> to the userList
            const li = document.createElement("li");
            li.innerText = user.name;
            userList.appendChild(li);
        });
    }catch(error){
        console.error("Error fetching users: ", error)
    }
}
fetchUsers();