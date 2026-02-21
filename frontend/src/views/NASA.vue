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
      <div
      v-if="apod.media_type === 'image'"
      class="apod-bg"
      :style="{ backgroundImage: `url(${apod.hdurl || apod.url})`        
      }"
      ></div>

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
  height: 100%;
  width: 100%;
  background: black;
  color: white;
  overflow: hidden;
  position: relative;
}

.apod-bg,
.apod-video {
  position: absolute;
  inset: 0;

  background-size: cover;
  background-position: center;
  background-repeat: no-repeat;
}

.content {
  position: relative;
  height: 100%;
  width: 100%;
}
.overlay {
  position: absolute;
  bottom: 20%;
  left: 50%;
  transform: translateX(-50%);

  width: 75%;   /* SAFE WIDTH */
  max-width: 75%;

  padding: 10px;
  background: rgba(254, 254, 254, 0.12);
  backdrop-filter: blur(8px);

  border-radius: 40px;

  display: flex;
  flex-direction: column;

  height: 80px;
  overflow: hidden;

  transition: height 0.3s ease;
}

.overlay.expanded {
  height: 40%;
  overflow-y: auto;
  backdrop-filter: blur(8px);
}



.overlay h2 {
  font-size: 18px;
  margin-bottom: 10px;
}

 .overlay p {
  font-size: 14px;
  line-height: 1.5;
}

.toggle-btn {
  align-self: flex-start;
  background: none;
  border: 1px solid rgba(196, 190, 190, 0.4);
  padding: 6px 14px;
  border-radius: 20px;
  color: white;
  cursor: pointer;
  font-size: 15px;
  transition: background 0.2s ease;
}

.toggle-btn:hover {
  background: rgb(226, 223, 223);
}
</style>