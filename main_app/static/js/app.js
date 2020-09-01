const sign_in_buton = document.querySelector("#sign-in-buton");
const sign_up_buton = document.querySelector("#sign-up-buton");
const conta = document.querySelector(".conta");

sign_up_buton.addEventListener("click", () => {
    conta.classList.add("sign-up-mode");
});

sign_in_buton.addEventListener("click", () => {
    conta.classList.remove("sign-up-mode");
});
