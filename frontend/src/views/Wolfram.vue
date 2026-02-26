<script>
import HomeButton from '../components/HomeButton.vue'

export default {
  components: { HomeButton },

  data() {
    return{
        userInput: '',
        result: '',
        loading: false,
        error: ''
    }
  },

  methods: {
    async askWolfram() {
        if (!this.userInput) return

        this.loading = true
        this.error = ''
        this.result = ''

        try {
            const response = await fetch(
                `http://localhost:8000/wolfram?query=${encodeURIComponent(this.userInput)}`
            )

            const data = await response.json()

            if (data.error) {
                this.error = data.error
            } else {
                this.result = data.result
            }
        } catch (err) {
            this.error = 'Server connection failed'
        }

        this.loading=false
    }
  }
}
</script>

<template>
  <div class="wolfram-container">

    <div class="wolfram-panel">
    <HomeButton />

    <h1>Wolfram</h1>

    <input
        v-model="userInput"
        placeholder="Ask Wolfram a question"
        @keyup.enter="askWolfram"
    />

    <button @click="askWolfram">
        Ask
    </button>

    <p v-if="loading"> class="loading-text">
        Thinking...
    </p>
    <p v-if="error" class="error-text">
        {{ error }}
    </p>

    <div v-if="result" class="result-box"> 
        {{ result }}
    </div>
    </div>

  </div>
</template>

<style scoped>
.wolfram-container{
    position: absolute;
    inset: 0;

    display: flex;
    align-items: center;
    justify-content: center;

    background-image: url('../assets/aube/wolfram_background.png');
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
}

.wolfram-panel {
    width: 65%;
    max-width: 500px;

    padding: 40px;

    background: rgba(220, 218, 218, 0.45);
    backdrop-filter: blur(8px);
    
    border-radius: 24px;
    box-shadow: 0 15px 40px rgba(65, 65, 65, 0.5);

    text-align: center;
    color: white;
}

.wolfram-panel h1{
    margin-bottom: 25px;
    font-size: 28px;
    font-weight: 600;
}

.wolfram-panel input{
    width: 100%;
    padding: 14px 18px;
    margin-top: 10px;

    border-radius: 18px;
    border: none;

    background: rgba(28, 27, 27, 0.244);
    color: white;
    font-size: 16px;

    outline: none;
}

.wolfram-panel button {
    margin-top: 18px;
    padding: 12px 26px;

    border-radius: 20px;
    border: none;

    background: rgba(27, 27, 27, 0.273);
    color: white;
    font-size: 15px;
    font-weight: 500;

    cursor: pointer;
    transition: all 0.2s ease;
}

.wolfram-panel button:hover {
    background: rgba(33, 32, 32, 0.226);
    transform: translateY(-2px);
}

.result-box {
    margin-top: 28px;
    padding: 18px;

    background: rgba(20, 20, 20, 0.232);
    border-radius: 20px;

    font-size: 18px;
    line-height: 1.4;
}

.loading-text {
    margin-top: 18px;
    opacity: 0.4;
}

.error-text {
    margin-top: 18px;
    color: #ff7b7b;
}

</style>