<template>
  <div class="device-frame">
    <transition name="fade" mode="out-in">
      <router-view />
    </transition>
  </div>
</template>

<style>
.fade-enter-active,
.fade-leave-active {
  transition: opacity 0.25s ease;
}

.fade-enter-from,
.fade-leave-to {
  opacity: 0;
}

/* 🔒 Lock entire app to viewport */
#app {
  height: 100vh;
  width: 100vw;
  overflow: hidden;
}

.device-frame {
  position: relative;
  height: 100vh;
  width: 100vw;

  overflow: hidden;
  background: black;

  border-radius: 50%;
  clip-path: circle(50%);

}
</style>