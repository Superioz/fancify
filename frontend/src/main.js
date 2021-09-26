import Vue from "vue";
import App from "./App.vue";

import { store } from "./store";

// Vue component that connects to the `app` element
// and renders the `App` component into it.
//
// The `h` stands for `hyperscript` which is a library to
// generate HTML structures.
new Vue({
    el: "#app",
    render: (h) => h(App),
    store,
});
