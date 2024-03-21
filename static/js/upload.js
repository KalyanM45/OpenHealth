document
        .getElementById("customButton")
        .addEventListener("click", function () {
          document.getElementById("file").click();
        });

      document.getElementById("file").addEventListener("change", function () {
        const fileInput = document.getElementById("file");
        const fileName = fileInput.files[0]?.name || "Not selected file";
        const fileLabel = document.querySelector(".footer p");
        fileLabel.textContent = fileName;
      });

      const viewButton = document.querySelector(".footer svg");
      viewButton.addEventListener("click", function (event) {
        event.preventDefault();

        const fileInput = document.getElementById("file");
        const file = fileInput.files[0];

        if (file) {
          const fileType = file.type.split("/")[0];
          if (fileType === "image") {
            const imageUrl = URL.createObjectURL(file);
            window.open(imageUrl, "_blank");
          } else if (
            fileType === "application" &&
            file.type === "application/pdf"
          ) {
            const pdfUrl = URL.createObjectURL(file);
            window.open(pdfUrl, "_blank");
          } else {
            alert("Cannot display this file type");
          }
        } else {
          alert("No file selected");
        }
      });

      const deleteButton = document.querySelector(".delete-button");
      deleteButton.addEventListener("click", function (event) {
        event.preventDefault();
        const fileInput = document.getElementById("file");
        fileInput.value = null;
        const fileLabel = document.querySelector(".footer p");
        fileLabel.textContent = "No file selected";
      });

      document.getElementById("redirectmore").addEventListener("click", function() {
        window.open("../templates/llm.html", "_blank");
    });