let cart = [];

function addToCart(name, price) {
  cart.push({ name, price });
  renderCart();
}

function removeItem(index) {
  cart.splice(index, 1);
  renderCart();
}

function renderCart() {
  const list = document.getElementById("cartItems");
  const total = document.getElementById("total");
  list.innerHTML = "";
  let sum = 0;
  cart.forEach((item, i) => {
    sum += item.price;
    list.innerHTML += `<li>${item.name} - $${item.price} <button class="btn_rm" onclick="removeItem(${i})">Remove</button></li>`;
  });
  total.textContent = sum;
}