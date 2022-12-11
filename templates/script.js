const text = document.getElementById("text");
const button = document.getElementById("button");
const result = document.getElementById("result");

const sentiments = ["&#128577", "&#128528", "&#128578"];

button.onclick = async () => {
  const response = await fetch("/", {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify({ data: text.value }),
  });

  result.innerHTML = sentiments[(await response.json()).value];
};
