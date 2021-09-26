import Vue from "vue";
import Vuex from "vuex";
import VuexPersistance from "vuex-persist";

Vue.use(Vuex);

const vuexLocal = new VuexPersistance({
    storage: window.localStorage,
});

export const store = new Vuex.Store({
    state: {
        history: [],
    },
    mutations: {
        addToHistory(state, payload) {
            state.history.push(payload);
        },
        clearHistory(state) {
            state.history = [];
        },
    },
    plugins: [vuexLocal.plugin],
});