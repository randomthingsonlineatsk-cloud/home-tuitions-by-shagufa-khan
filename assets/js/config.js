// Single place to edit your social links / contact info.
// Just edit this file (via GitHub's web editor) and the whole site updates.
const SITE_CONFIG = {
  brandName: "Home Tuitions by Shagufa Khan",
  tagline: "Free notes, solutions and video lessons — Class 1 to NEET, JEE, B.Sc & M.Sc",
  youtubeUrl: "https://www.youtube.com/@hometuitionsbyshagufakhan",
  instagramUrl: "https://www.instagram.com/hometuitionsbyshagufakhan",
  contactEmail: "hometuitionsbyshagufakhan@gmail.com",
  // base path so links work whether the repo is served at the domain root or under /repo-name/
  basePath: (function () {
    const path = window.location.pathname;
    const marker = "/home-tuitions-by-shagufa-khan/";
    const idx = path.indexOf(marker);
    return idx === -1 ? "/" : path.slice(0, idx + marker.length);
  })(),
};
