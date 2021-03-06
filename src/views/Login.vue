<template>
  <div>
    <v-card class="pa-6">
      <v-form>
        <v-row>
          <v-col xs="12" sm="6">
            <v-text-field
              v-model="email"
              :error-messages="emailErrors"
              label="E-mail"
              required
            ></v-text-field
          ></v-col>
          <v-col xs="12" sm="6">
            <v-text-field
              v-model="password"
              :error-messages="passwordErrors"
              :append-icon="showPassword ? 'mdi-eye' : 'mdi-eye-off'"
              :type="showPassword ? 'text' : 'password'"
              label="Password"
              required
              @click:append="showPassword = !showPassword"
            ></v-text-field>
          </v-col>
        </v-row>

        <v-row>
          <v-col cols="2">
            <v-btn
              color="primary"
              class="mr-1"
              :loading="loading"
              :disabled="$v.$invalid"
              @click="login"
              >Login</v-btn
            >
            <v-btn disabled>Register</v-btn>
          </v-col>
        </v-row>
        <v-row>
          <v-col>
            Note: Cookies will only be used to store your login status and personal preferences, we will not track you using Cookies.
          </v-col>
        </v-row>
      </v-form>
    </v-card>
  </div>
</template>

<script>
import { validationMixin } from "vuelidate";
import { required, email } from "vuelidate/lib/validators";

export default {
  mixins: [validationMixin],
  validations: {
    email: {
      required,
      email,
    },
    password: {
      required,
    },
  },
  data() {
    return {
      password: "",
      email: "",
      emailErrors: [],
      passwordErrors: [],
      showPassword: false,
      loading: false,
    };
  },
  mounted() {
    this.$socket.disconnect();
  },
  methods: {
    login() {
      this.loading = true;
      this.$store
        .dispatch("user/login", {
          email: this.email,
          password: this.password,
        })
        .then(
          () => {
            this.loginOk();
          },
          (err) => {
            const payload = err.response.data.payload;
            if (payload.errors) {
              this.emailErrors = payload.errors.email || [];
              this.passwordErrors = payload.errors.password || [];
            }

            if (payload.error) {
              if (payload.error.endsWith("not logged in.")) {
                this.loginOk();
              }
            }
          }
        )
        .finally(() => {
          this.loading = false;
        });
    },
    loginOk() {
      this.$router.replace("/");
      this.$socket.connect();
      this.$notify("success", "You are logged in.");
    },
  },
};
</script>

<style lang="scss" scoped></style>
