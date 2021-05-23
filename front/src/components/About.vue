<template>
  <body class="u-body">
    <hr style="background-color: #000000; border-top: 1px; margin-bottom: 50px;">
    <section class="u-align-center u-clearfix u-section-1" id="carousel_f2cc">
      <div class="u-container-style u-group u-palette-5-base u-shape-rectangle u-group-1">
        <div class="u-container-layout u-container-layout-1"></div>
      </div>
      <div class="u-clearfix u-layout-wrap u-layout-wrap-1">
        <div class="u-layout">
          <div class="u-layout-row">
            <div class="u-align-left u-container-style u-layout-cell u-right-cell u-size-30 u-layout-cell-1">
              <div class="u-container-layout u-valign-middle u-container-layout-2">
                <h2 class="u-custom-font u-font-playfair-display u-text u-text-1">About</h2>
                <p class="u-text u-text-2">Momently brings back memories that would otherwise get lost in time by writing your personal diary. It harnesses the power of data you input into your devices daily. We are a team of 4 passionate scientists and visionars. Help us create a better world for everyone.</p>
              </div>
            </div>
            <div class="u-container-style u-image u-layout-cell u-left-cell u-size-30 u-image-1">
              <div class="u-container-layout u-valign-bottom-md u-valign-top-sm u-valign-top-xs u-container-layout-3"></div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </body>
</template>

<script>
export default {
  name: 'About',
  props: {

  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>
.u-section-1 {
  min-height: 50%;
}

.u-section-1 .u-group-1 {
  min-height: 337px;
  width: 15%;
  background-image: none;
  margin: 0 auto 0 0;
}

.u-section-1 .u-container-layout-1 {
  padding: 30px;
}

.u-section-1 .u-layout-wrap-1 {
  width: 980px;
  margin: -337px calc(((100% - 1140px) / 2)) 0 auto;
}

.u-section-1 .u-layout-cell-1 {
  min-height: 640px;
}

.u-section-1 .u-container-layout-2 {
  padding-bottom: 30px;
}

.u-section-1 .u-text-1 {
  font-size: 6rem;
  line-height: 1;
  margin: 0;
}

.u-section-1 .u-text-2 {
  font-size: 1.125rem;
  line-height: 2.2;
  width: 100%;
  font-weight: 300;
  
}

#carousel_f2cc > div.u-clearfix.u-layout-wrap.u-layout-wrap-1 > div > div > div.u-align-left.u-container-style.u-layout-cell.u-right-cell.u-size-30.u-layout-cell-1 > div {
    padding-top: 0px;
    margin-top: 0px;
    align-content: top;
}

.u-section-1 .u-image-1 {
  min-height: 50%;
  background-image: url("./images/momently_about.jpg");
  background-position: 50% 50%;
}

.u-section-1 .u-container-layout-3 {
  padding: 30px 30px 30px 30px;
}

@media (max-width: 1199px) {
  .u-section-1 {
    min-height: 565px;
  }

  .u-section-1 .u-group-1 {
    background-position: 0% 49.64%;
    background-size: auto 270%;
  }

  .u-section-1 .u-layout-wrap-1 {
    width: 820px;
    margin-right: calc(((100% - 940px) / 2));
  }

  .u-section-1 .u-layout-cell-1 {
    min-height: 565px;
  }

  .u-section-1 .u-image-1 {
    min-height: 565px;
  }
}

@media (max-width: 991px) {
  .u-section-1 {
    min-height: 635px;
  }

  .u-section-1 .u-group-1 {
    min-height: 256px;
    width: calc(((100% - 720px) / 2) + 99px);
  }

  .u-section-1 .u-layout-wrap-1 {
    width: 621px;
    margin-top: -256px;
    margin-right: calc(((100% - 720px) / 2));
  }

  .u-section-1 .u-layout-cell-1 {
    min-height: 635px;
  }

  .u-section-1 .u-text-1 {
    font-size: 4.5rem;
  }

  .u-section-1 .u-image-1 {
    min-height: 635px;
  }
}

@media (max-width: 767px) {
  .u-section-1 {
    min-height: 568px;
  }

  .u-section-1 .u-group-1 {
    width: 123px;
  }

  .u-section-1 .u-container-layout-1 {
    padding-left: 10px;
    padding-right: 10px;
  }

  .u-section-1 .u-layout-wrap-1 {
    width: 423px;
    margin-right: calc(((100% - 540px) / 2));
  }

  .u-section-1 .u-layout-cell-1 {
    min-height: 409px;
  }

  .u-section-1 .u-container-layout-2 {
    padding-left: 10px;
    padding-right: 10px;
  }

  .u-section-1 .u-image-1 {
    min-height: 477px;
  }

  .u-section-1 .u-container-layout-3 {
    padding-left: 10px;
  }
}

@media (max-width: 575px) {
  .u-section-1 {
    min-height: 922px;
  }

  .u-section-1 .u-group-1 {
    min-height: 242px;
    width: 79px;
  }

  .u-section-1 .u-layout-wrap-1 {
    width: 291px;
    margin-top: -198px;
    margin-right: calc(((100% - 340px) / 2));
  }

  .u-section-1 .u-layout-cell-1 {
    min-height: 430px;
  }

  .u-section-1 .u-text-1 {
    font-size: 3rem;
  }

  .u-section-1 .u-image-1 {
    min-height: 360px;
  }
}
</style>
