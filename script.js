document.getElementById("generate-btn").addEventListener("click", () => {
    const length = parseInt(document.getElementById("length").value);
    const includeSpecial = document.getElementById("special-characters").checked;
  
    fetch("/generate-password", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ length, include_special: includeSpecial }),
    })
      .then((response) => response.json())
      .then((data) => {
        if (data.password) {
          document.getElementById("password-box").innerText = data.password;
        }
      })
      .catch((error) => {
        alert("Error generating password: " + error);
      });
  });
  
  document.getElementById("copy-btn").addEventListener("click", () => {
    const password = document.getElementById("password-box").innerText;
    navigator.clipboard.writeText(password).then(() => {
      alert("Password copied to clipboard!");
    });
  });
  