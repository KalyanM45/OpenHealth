document
        .getElementById("clickableButton")
        .addEventListener("click", function () {
          document.body.style.backgroundColor = "#000";
          document.getElementById("initialScreen").classList.add("hidden");

          setTimeout(function () {
            document.getElementById("initialScreen").style.display = "none";
            document.getElementById("screen2").classList.remove("hidden");

            setTimeout(function () {
              document.getElementById("screen2").style.opacity = "1";
              document.getElementById("openHealthText").style.opacity = "1";
            }, 100);
          }, 400);

          setTimeout(function () {
            window.location.href = "landing1.html";
          }, 4000);
        });