<template>
  <div class="hoppi-root">
    <div class="radial-container">
      <div class="center-circle"></div>

      <router-link to="/spotify" class="app-circle north">
  <img src="../assets/aube/spotify_icon.png" alt="Spotify" />
</router-link>

<router-link to="/nasa" class="app-circle east">
  <img src="../assets/aube/nasa_icon.png" alt="NASA" />
</router-link>

<router-link to="/cadence" class="app-circle south">
  <img src="../assets/aube/cadence_icon.png" alt="Cadence" />
</router-link>

<router-link to="/wolfram" class="app-circle west">
  <img src="../assets/aube/wolfram_icon.png" alt="Wolfram" />
</router-link>
    </div>
  </div>
</template>

<script>
export default {
  name: "Home",
};
</script>

<style>
.hoppi-root {
  height: 100vh;
  width: 100vw;
  background: url("../assets/aube/background.png") center center / cover no-repeat;
  display: flex;
  align-items: center;
  justify-content: center;
  overflow: hidden;
  font-family: system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
}

a {
  text-decoration: none;
}

/* Lock square ratio */
.radial-container {
  position: relative;
  width: min(90vmin, 900px);
  height: min(90vmin, 900px);
}

/* Center circle */
.center-circle {
  position: absolute;
  width: 10%;
  height: 10%;
  top: 50%;
  left: 50%;
  transform: translate(-50%, -50%);
  border-radius: 50%;

  background: transparent;
  box-shadow: 0 0 80px rgb(255, 255, 255);
}

/* App bubbles */
.app-circle {
  position: absolute;
  width: 22%;
  height: 22%;
  background: #ffffff;
  border-radius: 50%;
  display: flex;
  align-items: center;
  justify-content: center;
  box-shadow: 0 10px 30px rgba(0, 0, 0, 0.08);
  cursor: pointer;
  overflow: hidden;            /* THIS CLIPS IMAGE */
  user-select: none;
  transition: box-shadow 0.15s ease, filter 0.15s ease; /* removed transform */
}

.app-circle img {
  width: 100%;
  height: 100%;
  object-fit: cover;           /* fills circle */
  pointer-events: none;
}

.app-circle:active {
  box-shadow: 0 6px 18px rgba(0, 0, 0, 0.15) inset;
  filter: brightness(0.96);
}


/* Positions relative to square */

.north {
  top: 0%;
  left: 50%;
  transform: translate(-50%, 0);
}

.east {
  right: 0%;
  top: 50%;
  transform: translate(0, -50%);
}

.south {
  bottom: 0%;
  left: 50%;
  transform: translate(-50%, 0);
}

.west {
  left: 0%;
  top: 50%;
  transform: translate(0, -50%);
}
</style>