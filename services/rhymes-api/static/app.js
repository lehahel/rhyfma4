// show a message with a type of the input
function showMessage(input, message, type) {
	// get the small element and set the message
	const msg = input.parentNode.querySelector("small");
	msg.innerText = message;
	// update the class for the input
	input.className = type ? "success" : "error";
	return type;
}

function showError(input, message) {
	return showMessage(input, message, false);
}

function showSuccess(input) {
	return showMessage(input, "", true);
}

function hasValue(input, message) {
	if (input.value.trim() === "") {
		return showError(input, message);
	}
	return showSuccess(input);
}

function validateEmail(input, requiredMsg, invalidMsg) {
	// check if the value is not empty
	if (!hasValue(input, requiredMsg)) {
		return false;
	}
	// validate email format
	const emailRegex =
		/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/;

	const email = input.value.trim();
	if (!emailRegex.test(email)) {
		return showError(input, invalidMsg);
	}
	return true;
}

const form1 = document.querySelector("#get_rhyme");

const NAME_REQUIRED = "Please enter word";
const EMAIL_REQUIRED = "Please enter your email";
const EMAIL_INVALID = "Please enter a correct email address format";

form1.addEventListener("submit", function (event) {
	event.preventDefault();
	let nameValid = hasValue(form1.elements["name"], NAME_REQUIRED);
  if (nameValid) {
		fetch(url='http://127.0.0.1:5000/api/rhymes?word=' + form1.elements["name"].value.trim(""), {
      method: 'GET'
    })
		.then(data => data.json())
		.then(result => {
			console.log(result.rhyme);
			form1.elements["name"].value = result.rhyme;
		})
	}
});

const form2 = document.querySelector("#add_rhyme");

form2.addEventListener("submit", function (event) {
	event.preventDefault();
	let nameValid = hasValue(form2.elements["name1"], NAME_REQUIRED);
  if (nameValid) {
		fetch(url='http://127.0.0.1:5000/api/rhymes?word=' + form2.elements["name1"].value.trim("") + '&rhyme=' + form2.elements["name2"].value.trim(""), {
      method: 'POST'
    });
	}
});
