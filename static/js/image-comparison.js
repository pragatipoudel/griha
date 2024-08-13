    const slider = document.querySelector(".image-comparison-wrapper .slider input");
    const img = document.querySelector(".image-comparison-wrapper .images .img-2");
    const dragLine = document.querySelector(".image-comparison-wrapper .slider .drag-line");

    slider.addEventListener('input', (e) => {
        let sliderVal = e.target.value;
        dragLine.style.left = sliderVal + "%";
        img.style.width = sliderVal + "%";
    });

    