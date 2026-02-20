<template>
  <router-link to="/" class="home-orb">
    ⟵
  </router-link>
</template>

<style>
.home-orb {
  position: fixed;
  top: 24px;
  left: 24px;
  width: 52px;
  height: 52px;
  border-radius: 50%;
  background: rgba(255, 255, 255, 0.6);
  backdrop-filter: blur(6px);
  display: flex;
  align-items: center;
  justify-content: center;
  font-size: 20px;
  text-decoration: none;
  color: #2f3e4d;
  box-shadow: 0 6px 18px rgba(0,0,0,0.1);
  transition: box-shadow 0.15s ease, filter 0.15s ease;
}

.home-orb:active {
  box-shadow: inset 0 4px 10px rgba(0,0,0,0.15);
  filter: brightness(0.95);
}
</style>