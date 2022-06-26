<template>
  <div>
    <!-- nav start -->
    <nav id="header" class="w-full text-white bg-white">
      <div
        class="
          w-full
          container
          mx-auto
          flex flex-wrap
          items-center
          justify-between
          px-2
        "
      >
        <a href="#">
          <img class="w-52 m-2" src="../assets/logo.png" alt="" />
        </a>

        <div class="block lg:hidden">
          <button
            id="nav-toggle"
            class="
              flex
              items-center
              px-3
              py-2
              border
              rounded
              text-gray-500
              border-gray-600
              hover:text-gray-800 hover:border-green-500
              appearance-none
              focus:outline-none
            "
          >
            <svg
              class="fill-current h-3 w-3"
              viewBox="0 0 20 20"
              xmlns="http://www.w3.org/2000/svg"
            >
              <title>Menu</title>
              <path d="M0 3h20v2H0V3zm0 6h20v2H0V9zm0 6h20v2H0v-2z" />
            </svg>
          </button>
        </div>

        <div
          class="
            w-full
            flex-grow
            lg:flex lg:items-center lg:w-auto
            hidden
            mt-2
            lg:mt-0
            text-black
            p-4
            lg:p-0
            z-20
          "
          id="nav-content"
        >
          <ul class="list-reset lg:flex justify-end flex-1 items-center">
            <li class="mr-3" v-for="(n, idx) in navs" :key="idx">
              <a
                class="
                  inline-block
                  text-black
                  no-underline
                  hover:text-gray-800 hover:text-underline
                  py-2
                  px-2
                "
                :href="n.link"
                >{{ n.l }}</a
              >
            </li>
          </ul>
        </div>
      </div>
    </nav>
    <!-- end nav -->
    <!-- Start section1 -->
    <div class="relative overflow-hidden mt-2" id="home">
      <img
        src="../assets/header.jpeg"
        alt="Avatar"
        style="height: 572px"
        class="object-cover w-full"
      />
      <div
        class="
          absolute
          h-full
          py-2.5
          top-0
          justify-center
          flex
          inset-x-0
          text-white text-center
          leading-4
        "
        style="max-width: 80%"
      >
        <div class="mt-36 lg:w-4/6 xl:w-4/6 text-left mx-3">
          <p class="text-4xl md:text-2xl pt-7 xl:text-5xl lg:text-2xl">
            The Way to Make Dreams Happen
          </p>
          <router-link to="/login"
            ><button
              class="text-xl p-3 mt-10 rounded-full"
              style="background: #2fb3ff"
            >
              Start Now
            </button></router-link
          >
        </div>
      </div>
    </div>
    <!-- End section1 -->
    <!-- service section start -->
    <div class="bg-gray-100 w-full mt-10" style="color: #34434c">
      <div class="flex justify-center">
        <p class="text-4xl text-center mt-16">Are you ready to get started ?</p>
      </div>
      <center>
        <p class="text-center w-2/3 pt-8">
          with our ultimate community edition you can test functions from MAZU™
          for free and build up your own future online community.
        </p>
      </center>
      <div class="flex justify-center">
        <router-link
          to="/login"
          class="py-3 px-5 my-5 text-white rounded-full mb-14"
          style="background: #2fb3ff"
          >Try it now
        </router-link>
      </div>
    </div>
    <div class="w-full" style="height: 122px; background: #30b4ff"></div>
    <center>
      <div class="w-full bg-gray-100" id="team">
        <p class="uppercase pt-10 text-3xl">moyats team</p>
        <div
          class="
            grid
            h-full
            md:grid-cols-2
            grid-cols-1
            lg:grid-cols-3
            xl:grid-cols-3
            gap-3
            w-2/3
            justify
          "
        >
          <div class="my-10" v-for="(mem, i) in members" :key="i">
            <div class="mt-5"></div>
            <img src="../assets/sef.jpg" alt="" />
            <div class="bg-white pb-3">
              <p class="text-xl py-2 text-center" v-text="mem.name"></p>
              <p class="text-sm pb-3 text-center" v-text="mem.position"></p>
              <div class="flex flex-row justify-center gap-3">
                <a :href="mem.facebook">
                  <img src="../assets/files/Vector-1.png" alt="" />
                </a>
                <a :href="mem.twitter">
                  <img src="../assets/files/Vector-2.png" alt="" />
                </a>
                <a :href="mem.instagram">
                  <img src="../assets/files/Group.png" alt="" />
                </a>
                <a :href="mem.linkedIn">
                  <img src="../assets/files/Group-123.png" alt="" />
                </a>
              </div>
            </div>
          </div>
          <!-- <div class="border-2 text-white mt-24 mx-1" v-for="x in 6" :key="x">
            <div class="my-12">
            </div>
          </div> -->
          <div class="mb-10"></div>
        </div>
      </div>
    </center>

    <div
      class="
        h-full
        py-2.5
        top-0
        justify-center
        flex
        inset-x-0
        text-white text-center
        leading-4
      "
    >
      <div>
        <center>
          <div class="w-3/4">
            <div class="grid xl:grid-cols-2 gap-20 lg:grid-cols-2 mt-10">
              <div class="my-12 bg-white text-black">
                <p class="text-2xl py-5">Subscribe to Newsletter</p>
                <p class="text-gray-600">Weekly Freebies and More!</p>
                <center>
                  <div class="w-full">
                    <div class="mt-2"></div>
                    <input
                      placeholder="full name"
                      type="text"
                      name=""
                      class="
                        h-8
                        rounded-full
                        p-5
                        text-gray-600
                        my-2
                        w-full
                        bg-gray-200
                      "
                      id=""
                    />
                    <input
                      type="text"
                      name=""
                      placeholder="Email"
                      class="
                        h-8
                        rounded-full
                        p-5
                        text-gray-600
                        my-2
                        w-full
                        bg-gray-200
                      "
                      id=""
                    />
                    <input
                      type="text"
                      name=""
                      placeholder="Department"
                      class="
                        h-8
                        rounded-full
                        p-5
                        text-gray-600
                        my-2
                        w-full
                        bg-gray-200
                      "
                      style="text-decoration: none"
                      id=""
                    />
                    <textarea
                      name=""
                      id=""
                      class="
                        rounded-xl
                        p-5
                        text-gray-600
                        my-2
                        leading-6
                        w-full
                        bg-gray-200
                      "
                      style="text-decoration: none"
                      cols="30"
                      rows="10"
                    ></textarea>
                    <button
                      class="
                        uppercase
                        p-3
                        w-full
                        mt-2
                        mb-10
                        rounded-full
                        text-white text-sm
                      "
                      style="background: #30b4ff"
                    >
                      Subscribe now
                    </button>
                  </div>
                </center>
              </div>
              <div class="text-left lg:mt-32 xl:mt-32 text-black">
                <div class="bg-white">
                  <p>Location</p>
                  <p class="text-md text-gray-500 py-4">
                    Gerji, Addis Ababa, Ethiopia
                  </p>
                </div>
                <div class="bg-white mt-3">
                  <p>E-mail</p>
                  <p class="text-md text-gray-500 py-4">
                    moyatsolutions@gmail.com
                  </p>
                </div>
                <div class="bg-white mt-3">
                  <p>Phone</p>
                  <p class="text-md text-gray-500 py-4">+251942762357</p>
                </div>
                <div class="flex flex-row mb-10 gap-3 hidden">
                  <a :href="socials.facebook" target="_blank">
                    <img src="../assets/files/Group-10.png" alt="" />
                  </a>
                  <a :href="socials.twitter" target="_blank">
                    <img src="../assets/files/Group-9.png" alt="" />
                  </a>
                  <a :href="socials.instagram" target="_blank">
                    <img src="../assets/files/Group-7.png" alt="" />
                  </a>
                  <a :href="socials.linkedin" target="_blank">
                    <img src="../assets/files/Group-8.png" alt="" />
                  </a>
                </div>
              </div>
            </div>
          </div>
        </center>
      </div>
    </div>
    <!-- footer start -->
    <center>
      <div
        class="
          lg:mx-20
          xl:mx-20
          grid
          md:grid-cols-2
          lg:grid-cols-4
          xl:grid-cols-4
          gap-4
          mt-20
        "
        style="
          background-image: linear-gradient(
            180deg,
            #ffffff 0%,
            #ffffff 25.52%,
            #ffffff 73.96%,
            #f1f9fe 100%
          );
        "
      >
        <div class="w-3/4">
          <ul class="px-3 text-left">
            <li class="xl:pl-4 lg:pl-4 flex items-center">
              <a
                class="
                  text-white
                  no-underline
                  hover:no-underline
                  font-bold
                  text-2xl
                  lg:text-4xl
                "
                href="#"
              >
                <img class="w-full" src="../assets/logo.png" alt="" />
              </a>
            </li>
            <li class="xl:px-6 pt-2 lg:px-6 text-sm text-gray-600 leading-6">
              We offer full-service and digital customer support with a
              comprehensive range of services.
            </li>
            <li>
              <div class="xl:px-6 pt-2 lg:px-6 flex flex-row mb-10 gap-3">
                <a :href="socials.facebook" target="_blank">
                  <img src="../assets/files/Group-10.png" alt="" />
                </a>
                <a :href="socials.twitter" target="_blank">
                  <img src="../assets/files/Group-9.png" alt="" />
                </a>
                <a :href="socials.instagram" target="_blank">
                  <img src="../assets/files/Group-7.png" alt="" />
                </a>
                <a :href="socials.linkedin" target="_blank">
                  <img src="../assets/files/Group-8.png" alt="" />
                </a>
              </div>
            </li>
          </ul>
        </div>
        <ul class="p-3 text-left text-gray-500">
          <li class="uppercase text-black">Contact Us</li>
          <li class="py-3">Gerji, Addis Ababa, Ethiopia</li>
        </ul>
        <ul class="p-3 text-left text-gray-500">
          <li class="uppercase text-black">Powered By</li>
          <li class="py-3">Moyat Software Solutions</li>
        </ul>
      </div>
    </center>
  </div>
</template>
<script lang="ts">
import { defineComponent } from "vue";

export default defineComponent({
  methods: {},
  data: () => ({
    options: [
      "MAZU Community",
      "Development",
      "Graphic Design",
      "Job Application",
      "Chat Support Request",
      "Mail Support Request",
      "In/Outbound Request",
      "Media Management Request",
      "Translation Service",
    ],
    name: "",
    email: "",
    message: "",
    department: "",
    socials: {
      twitter: "https://twitter.com/_Dialogmakers",
      instagram: "https://www.instagram.com/dialogmakers_global/",
      facebook: "https://www.facebook.com/DialogmakersGlobal",
      linkedin:
        "https://www.linkedin.com/in/dialogmakers-international-7b2398201",
    },
    members: [
      {
        pic: "Rectangle-1.png",
        name: "Amar Mahdi",
        position: "Lead Developer",
        facebook: "https://www.facebook.com/DialogmakersGlobal",
        twitter: "https://twitter.com/flirttool",
        instagram: "https://www.instagram.com/dialogmakers_global/",
        linkedIn: "mailto:joe.hsu@dialogmakers-international.com",
      },
      {
        pic: "sef.jpg",
        name: "Amen Abe",
        position: "Lead Developer",
        facebook: "https://www.facebook.com/DialogmakersGlobal",
        twitter: "https://twitter.com/flirttool",
        instagram: "https://www.instagram.com/dialogmakers_global/",
        linkedIn: "mailto:eric.roennau@dialogmakers-international.com",
      },
      {
        pic: "Rectangle-3.png",
        name: "Ephrem Berhanu",
        position: "Lead Graphics & UI",
        facebook: "https://www.facebook.com/DialogmakersGlobal",
        twitter: "https://twitter.com/flirttool",
        instagram: "https://www.instagram.com/dialogmakers_global/",
        linkedIn: "mailto:nicole@dialogmaker-international.com",
      },
    ],
    reasons: [
      {
        head: "Inbound Telemarketing",
        lsts: ["Telesales, technical support, 2. Level operations"],
      },
      {
        head: "Full Stack Development",
        lsts: ["System Design, full stack development and consulting"],
      },
      {
        head: "Media Marketing",
        lsts: [
          "Worldwide online press releases in over 360 mayor newsletter and online magazines.",
        ],
      },
      {
        head: "Outbound Telemarketing",
        lsts: ["Sales, lead generation, telemarketing, cold calls, fundrasing"],
      },
      { head: "Email Support", lsts: ["Customer care, Support"] },
      {
        head: "Chat Support",
        lsts: [
          "Chat support in real-time via instant messaging, website pop-up dialogue box etc",
        ],
      },
      {
        head: "Social Media Marketing",
        lsts: [
          "Setup, planing and direction of social media channels and campaigns.",
        ],
      },
      {
        head: "Graphic Design",
        lsts: ["UI Graphics, brand identity graphics, advertisement graphics"],
      },
      {
        head: "Translation services",
        lsts: [
          "Professional translations:",
          "English - Japanese",
          "German - Chinese",
          "German - English",
          "German - Chinese",
          "English - Mandarin",
          "English - Tagalog",
        ],
      },
    ],
    navs: [
      { l: "Login", link: "/login" },
      { l: "Register", link: "/login" },
    ],
    values: [
      {
        v: 100,
        lbl: "Faster",
        suf: "%",
      },
      {
        v: 700,
        lbl: "Cups of Coffee",
        suf: "",
      },
      {
        v: 800000,
        lbl: "Active Clients",
        suf: "",
      },
      {
        v: "6",
        lbl: "Employed countries",
        suf: "",
      },
    ],
  }),
});
</script>

<style scoped>
/* SMARTPHONES PORTRAIT */
@media only screen and (min-width: 300px) {
  .subscribeBox {
    height: 900px;
  }
}

/* SMARTPHONES LANDSCAPE */
@media only screen and (min-width: 480px) {
  .subscribeBox {
    height: 800px;
  }
}

/* TABLETS PORTRAIT */
@media only screen and (min-width: 768px) {
  .subscribeBox {
    height: 850px;
  }
}

/* TABLET LANDSCAPE / DESKTOP */
@media only screen and (min-width: 1024px) {
  .subscribeBox {
    height: 550px;
  }
}
</style>
