<script>
import HomeButton from '../components/HomeButton.vue'

export default {
  components: { HomeButton },

  data() {
    return {
      apod: null,
      loading: true,
      error: null,
      expanded: false
    }
  },
  async mounted() {
    try {
      const response = await fetch(
        `https://api.nasa.gov/planetary/apod?api_key=${import.meta.env.VITE_NASA_KEY}`
      )

      if (!response.ok) {
        throw new Error("NASA API error")
      }

      const data = await response.json()
      this.apod = data

    } catch (err) {
      this.error = "Unable to retrieve cosmic data."
      console.error(err)
    } finally {
      this.loading = false
    }
  }
}
</script>

<template>
  <div class="nasa-page">
    <HomeButton />

    <div v-if="loading" class="loading">
      Contacting deep space...
    </div>

    <div v-else-if="error" class="error">
      {{ error }}
    </div>

    <div v-else class="content">
      <img
        v-if="apod.media_type === 'image'"
        :src="apod.hdurl || apod.url"
        :alt="apod.title"
        class="apod-image"
      />

      <iframe
        v-else
        :src="apod.url"
        frameborder="0"
        allowfullscreen
        class="apod-video"
      ></iframe>

      <div
  class="overlay"
  :class="{ expanded: expanded }"
>
  <h2>{{ apod.title }}</h2>

  <p v-if="expanded">
    {{ apod.explanation }}
  </p>

  <button class="toggle-btn" @click="expanded = !expanded">
    {{ expanded ? 'Minimize' : 'Read More' }}
  </button>
</div>
    </div>
  </div>
</template>

<style>
.nasa-page {
  height: 100vh;
  width: 100vw;
  background: rgb(0, 0, 0);
  color: white;
  overflow: hidden;
  position: relative;
}

.apod-image,
.apod-video {
  width: 100%;
  height: 100%;
  object-fit: cover;
}

.overlay {
  position: absolute;
  bottom: 0;
  left: 0;
  width: 100%;

  padding: 24px;
  background: rgba(254, 254, 254, 0.11);

  transition: height 0.35s ease, padding 0.35s ease;
  overflow: hidden;

  display: flex;
  flex-direction: column;
  justify-content: flex-start;

  height: 110px; /* collapsed height */
}

.overlay.expanded {
  height: 50vh; /* expanded height */
  overflow-y: auto;
  backdrop-filter: blur(6px);
}

.overlay h2 {
  font-size: 22px;
  margin-bottom: 10px;
}

.overlay p {
  font-size: 15px;
  line-height: 1.6;
  opacity: 0.9;
  margin-bottom: 16px;
}

.toggle-btn {
  align-self: flex-start;
  background: none;
  border: 1px solid rgba(196, 190, 190, 0.4);
  padding: 6px 14px;
  border-radius: 20px;
  color: white;
  cursor: pointer;
  font-size: 13px;
  transition: background 0.2s ease;
}

.toggle-btn:hover {
  background: rgb(255, 255, 255);
}
</style>