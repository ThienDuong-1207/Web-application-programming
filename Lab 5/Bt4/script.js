const questions = [
  {
    q: "What is 2 + 2?",
    options: ["3", "4", "5"],
    answer: 1
  },
  {
    q: "What is capital of France?",
    options: ["Paris", "Rome", "London"],
    answer: 0
  }
];

let current = 0;
let score = 0;

function renderQuestion() {
  const q = questions[current];
  let html = `<div class="question"><strong>${q.q}</strong><br>`;
  q.options.forEach((opt, i) => {
    html += `<input type="radio" name="answer" value="${i}"> ${opt}<br>`;
  });
  html += `</div>`;
  document.getElementById("quiz").innerHTML = html;
}

function nextQuestion() {
  const selected = document.querySelector('input[name="answer"]:checked');
  if (!selected) {
    alert("Please choose an answer");
    return;
  }
  if (parseInt(selected.value) === questions[current].answer) {
    score++;
  }
  current++;
  if (current < questions.length) {
    renderQuestion();
  } else {
    document.getElementById("quiz").innerHTML = "Quiz finished!";
    document.getElementById("score").textContent = `Your score: ${score}/${questions.length}`;
  }
}

renderQuestion();