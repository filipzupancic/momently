<template>
  <body class="u-body">
    <hr style="background-color: #000000; border-top: 1px">
    <section class="u-clearfix u-palette-1-base u-valign-middle-md u-valign-middle-sm u-valign-middle-xs u-section-1" id="carousel_3e5e">
      <div class="u-clearfix u-layout-wrap u-layout-wrap-1">
        <div class="u-layout">
          <div class="u-layout-row">
            <div class="u-align-center u-container-style u-layout-cell u-right-cell u-shape-rectangle u-size-27 u-layout-cell-1">
              <div class="u-container-layout u-valign-middle u-container-layout-1">
                <h2 class="u-text u-text-body-color u-text-1">Momently</h2>
                <h6 class="u-text u-text-body-color u-text-2">Bring back the memories.</h6>
                <div class="u-border-4 u-border-black u-line u-line-vertical u-line-1"></div>
                <p class="u-text u-text-body-color u-text-3">Write your diary with a single click.</p>
                <a href="http://localhost:8080/diary" class="u-border-2 u-border-black u-btn u-button-style u-none u-text-black u-text-hover-grey u-btn-1">Begin</a>
                <!--<p class="u-text u-text-4">Created by <a href="http://localhost:8080/" class="u-active-none u-border-1 u-border-white u-btn u-button-link u-button-style u-hover-none u-none u-text-body-alt-color u-btn-2" target="_blank">Official voice channel</a>
                </p>-->
              </div>
            </div>
            <div class="u-container-style u-layout-cell u-left-cell u-size-33 u-layout-cell-2">
              <div class="u-container-layout u-valign-middle-lg u-valign-middle-xl u-valign-top-md u-container-layout-2">
                <img class="u-expanded-width u-image u-image-1" src="./images/momently-cover.jpg" data-image-width="1000" data-image-height="1023">
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>
  </body>
</template>

<script>
export default {
  name: 'Home',
  props: {
    msg: String
  }
}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped>

</style>
