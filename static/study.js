let back = document.getElementById("back")

document.addEventListener("keydown", (e) => {
    if (e.code === "Space") {
        e.preventDefault()
        back.classList.toggle("is-flipped")
    } else if (e.key >= "1" && e.key <= "5") {
        const button = document.querySelector(
            'button[name="rating"][value="' + e.key + '"]'
        )
        if (button) {
            button.click()
        }
    }
})
