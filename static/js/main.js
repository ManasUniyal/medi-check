const img_upload_btn = document.getElementById("img_upload")
const upload_img = document.getElementById("image")
img_upload_btn.addEventListener("change", function () {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        reader.addEventListener("load", function () {
            upload_img.setAttribute("src", this.result);
        });
        reader.readAsDataURL(file);
    }
})

const predict_btn = document.getElementById("predict_btn")
const form = document.getElementById("submit_image_form")
predict_btn.onclick = function () {
    form.submit();
}