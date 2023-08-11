var fileDropArea = function () {
  var dropArea = document.querySelectorAll('.file-drop-area');
  var previewContainer = document.querySelectorAll('.preview-image-container');

  var chkAllDropArea = function chkAllDropArea(i) {
      let input = dropArea[i].querySelector('.file-drop-input'),
          message = dropArea[i].querySelector('.file-drop-message'),
          icon = dropArea[i].querySelector('.file-drop-icon'),
          selectButton = dropArea[i].querySelector('.file-drop-btn'),
          removeButton = dropArea[i].querySelector('.remove-upload-btn'),
          invalidFileSize = previewContainer[i].querySelector('.invalidFileSize'),
          invalidFileType = previewContainer[i].querySelector('.invalidFileType');

      message.innerHTML = "Arrasta y suelta el archivo aqui...";

      selectButton.addEventListener('click', function () {
          input.click();
      });

      removeButton.addEventListener('click', function () {
          input.value = '';
          invalidFileSize.style.display = 'none';
          invalidFileType.style.display = 'none';
          message.innerHTML = "Arrasta y suelta el archivo aqui...";

          let fileDropPreview = previewContainer[i].querySelector('.file-drop-preview');
          if (fileDropPreview && fileDropPreview.querySelector("img")) {

              fileDropPreview.querySelector("img").remove();
              fileDropPreview.className = "file-drop-icon";

              const originIcon = document.createElement("i");
              originIcon.className = "fa-solid fa-cloud-arrow-up";
              icon.appendChild(originIcon);
          }

      });

      input.addEventListener('change', function () {
          if (input.files && input.files[0] && ((input.files[0].type == "image/jpeg") || (input.files[0].type == "image/png"))) {
              var reader = new FileReader();

              reader.onload = function (e) {
                  var fileData = e.target.result;
                  var fileName = input.files[0].name;
                  message.innerHTML = fileName;

                  if (fileData.startsWith('data:image')) {
                      var image = new Image();
                      image.src = fileData;

                      image.onload = function () {
                          icon.className = 'file-drop-preview img-thumbnail rounded';
                          icon.innerHTML = '<img src="' + image.src + '" alt="' + fileName + '">';
                      };
                  }
              };

              reader.readAsDataURL(input.files[0]);
          }

          if (!input.files) { 
              console.error("This browser doesn't seem to support the `files` property of file inputs.");

          } else if (input.files[0]) {
              let file = input.files[0];
              if (file.size > 1000000) {
                  invalidFileSize.style.display = "block";
              } else if (!((file.type == "image/jpeg") || (file.type == "image/png"))) {
                  invalidFileType.style.display = "block";

              } else {
                  invalidFileSize.style.display = "none";
                  invalidFileType.style.display = "none";
              }
          }
      });
  };

  var previewImage = function previewImage(i) {
      // # preview image
      const uploadInput = previewContainer[i].querySelector('.file-drop-input');
      const previewImageElement = previewContainer[i].querySelector('.preview-image');

      uploadInput.addEventListener('change', function () {
          const [file] = uploadInput.files;

          if (file && ((file.type == "image/jpeg") || (file.type == "image/png"))) {
              previewImageElement.style.display = 'block';
              previewImageElement.src = URL.createObjectURL(file)
          }
      });

      // # remove preview image
      previewContainer[i].querySelector('.remove-upload-btn').addEventListener('click', function () {
          previewImageElement.src = '';
          previewImageElement.style.display = 'none';

      });
  }

  for (var i = 0; i < dropArea.length; i++) {
      chkAllDropArea(i);
      previewImage(i);
  }
}();  

