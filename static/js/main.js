//Handling image upload button
const img_upload_btn = document.getElementById("img_upload")
const upload_img = document.getElementById("image")
const predict_btn = document.getElementById("predict_btn")
const form = document.getElementById("submit_image_form")

//Handling image upload button
img_upload_btn.addEventListener("change", function () {
    const file = this.files[0];
    if (file) {
        const reader = new FileReader();
        reader.addEventListener("load", function () {
            upload_img.setAttribute("src", this.result);
        });
        reader.readAsDataURL(file);
        predict_btn.style.display = "block";
    } else {
        upload_img.src = "/static/images/default_image.gif";
        predict_btn.style.display = "none";
    }
})

//Handling prediction button
if(predict_btn) {
    predict_btn.onclick = function () {
        form.submit();
    }
}