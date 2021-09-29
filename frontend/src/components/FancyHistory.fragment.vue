<script>
export default {
    name: "FancyHistory",
    methods: {
        clearHistory() {
            console.log("clear");
            this.$store.commit("clearHistory");
        },
        getHistory() {
            return this.$store.state.history.filter(entry => !!entry);
        },
        getTimestamp(date) {
            return (new Date(date)).toLocaleString();
        },
    },
};
</script>

<template>
  <section id="fancy-history">
    <article
      v-for="entry in getHistory()"
      :key="entry.createdAt"
      class="fancy-history"
    >
      <label
        class="fancy-accent fancy-meta"
        v-text="getTimestamp(entry.createdAt)"
      />
      <div style="align-items: center; display: flex; flex-wrap: wrap">
        <div
          class="fancy-input"
          v-text="entry.input"
        />
        <div class="fancy-arrow">
          →
        </div>
        <div
          class="fancy-output"
          v-text="entry.output"
        />
      </div>
    </article>

    <a
      class="fancy-button"
      @click="clearHistory()"
    >Clear History</a>
  </section>
</template>

<style scoped>

    #fancy-history {
        margin: 1em -1em 0;
    }

    .fancy-arrow,
    .fancy-input,
    .fancy-output {
        color: #FFFFFF80;
        font-family: "+Jakarta Sans";
        font-weight: 500;
        line-height: 1;
    }

    .fancy-arrow {
        display: none;
        font-size: 1.5em;
        margin: 0 .5em 4px;
    }

    .fancy-button {
        background-color: #D33A3A;
        margin: 1em 1em 0;
    }

    .fancy-button:hover {
        background-color: #9E1818;
    }

    .fancy-history {
        background-color: #48B3D533;
        padding: 1em;
    }

    .fancy-history ~ .fancy-history {
        margin-top: 1px;
    }

    .fancy-input {
        font-size: 1.25em;
    }

    .fancy-meta {
        display: block;
        font-size: .85em;
        font-weight: 400;
        margin-bottom: .75em;
    }

    .fancy-output {
        color: #FFF;
        font-feature-settings: "salt";
        font-size: 1.5em;
        font-weight: 600;
        margin-top: .25em;
        width: 100%;
    }

    @media screen and (min-width: 800px) {
        #fancy-history {
            margin: 1em -1em;
        }

        .fancy-arrow {
            display: block;
        }

        .fancy-button {
            margin: 1em;
        }

        .fancy-history ~ .fancy-history {
            margin-top: 1em;
        }

        .fancy-input {
            font-size: 1.5em;
        }

        .fancy-output {
            margin: 0;
            width: unset;
        }
    }

</style>
