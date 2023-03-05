const buttons = document.querySelectorAll("button")

buttons.forEach(button => {
    button.addEventListener("mouseover", () => {
        button.classList.add("active_btn")
    })

    button.addEventListener("mouseleave", () => {
        button.classList.remove("active_btn")
    })
})