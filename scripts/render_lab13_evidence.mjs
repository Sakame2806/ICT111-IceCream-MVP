import fs from "node:fs/promises";
import path from "node:path";
import sharp from "sharp";

const root = path.resolve(import.meta.dirname, "..");
const screenshots = path.join(root, "screenshots");

function svgText(text, x, y, size, options = {}) {
  const { fill = "#172033", weight = 400, anchor = "start" } = options;
  const escaped = text
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;");
  return `<text x="${x}" y="${y}" fill="${fill}" font-family="Arial, sans-serif" font-size="${size}" font-weight="${weight}" text-anchor="${anchor}">${escaped}</text>`;
}

const demoCards = [
  ["Home-Page.png", "Gallery entry", "FR-01 · FR-05"],
  ["Sign-Up.png", "Alias account", "FR-10 · FR-15"],
  ["Upload.png", "Multi-image upload", "FR-03 · FR-04 · FR-11"],
  ["Artwork-view.png", "Artwork detail", "FR-05 · FR-13"],
  ["User-Profile.png", "Creator profile", "FR-05 · FR-13"],
  ["User-Dashboard.png", "Creator summary", "FR-12 · FR-16"],
];

const demoComposite = [];
let demoSvg = `<svg width="1400" height="1000" xmlns="http://www.w3.org/2000/svg">
<rect width="1400" height="1000" fill="#f3f8fc"/>
${svgText("ICECREAM · LAB 13", 70, 64, 15, { fill: "#1789df", weight: 800 })}
${svgText("Final prototype demo flow", 70, 112, 44, { weight: 800 })}
${svgText("Start server → Publish → Discover → Review", 1330, 108, 18, { fill: "#607087", anchor: "end" })}`;

for (let i = 0; i < demoCards.length; i += 1) {
  const col = i % 3;
  const row = Math.floor(i / 3);
  const x = 70 + col * 430;
  const y = 155 + row * 365;
  const [file, title, req] = demoCards[i];
  const thumb = await sharp(path.join(screenshots, file))
    .resize(380, 230, { fit: "cover", position: "north" })
    .png()
    .toBuffer();
  demoComposite.push({ input: thumb, left: x + 15, top: y + 15 });
  demoSvg += `<rect x="${x}" y="${y}" width="410" height="330" rx="22" fill="#ffffff" stroke="#dce7ef" stroke-width="2"/>
  <rect x="${x + 15}" y="${y + 15}" width="380" height="230" rx="12" fill="#e5edf3"/>
  <rect x="${x + 18}" y="${y + 264}" width="38" height="38" rx="11" fill="#1789df"/>
  ${svgText(String(i + 1), x + 37, y + 290, 18, { fill: "#ffffff", weight: 800, anchor: "middle" })}
  ${svgText(title, x + 70, y + 283, 20, { weight: 800 })}
  ${svgText(req, x + 70, y + 305, 13, { fill: "#6c7b8d" })}`;
  if (col < 2) {
    demoSvg += `<circle cx="${x + 420}" cy="${y + 165}" r="18" fill="#172033"/>
    ${svgText("→", x + 420, y + 172, 20, { fill: "#ffffff", weight: 800, anchor: "middle" })}`;
  }
}
demoSvg += `<rect x="70" y="900" width="1260" height="62" rx="14" fill="#172033"/>
${svgText("Demo note: the final presentation focuses on the implemented publish-and-discover pathway.", 95, 939, 16, { fill: "#dce7ef" })}
</svg>`;

await sharp({
  create: { width: 1400, height: 1000, channels: 4, background: "#f3f8fc" },
})
  .composite([
    { input: Buffer.from(demoSvg), left: 0, top: 0 },
    ...demoComposite,
  ])
  .png()
  .toFile(path.join(screenshots, "demo-flow.png"));

const evidenceSvg = `<svg width="1400" height="900" xmlns="http://www.w3.org/2000/svg">
<rect width="1400" height="900" fill="#172033"/>
${svgText("ICECREAM · LAB 13 TESTING EVIDENCE", 70, 65, 15, { fill: "#92c9ef", weight: 800 })}
${svgText("Strong value, clear final priorities.", 70, 120, 45, { fill: "#ffffff", weight: 800 })}
${svgText("20 anonymized validation records + read-only current prototype smoke test · 29 July 2026", 70, 158, 18, { fill: "#b8c4d3" })}
<g>
  <rect x="70" y="205" width="295" height="155" rx="18" fill="#222d43" stroke="#354158"/>
  <rect x="385" y="205" width="295" height="155" rx="18" fill="#222d43" stroke="#354158"/>
  <rect x="700" y="205" width="295" height="155" rx="18" fill="#222d43" stroke="#354158"/>
  <rect x="1015" y="205" width="315" height="155" rx="18" fill="#222d43" stroke="#354158"/>
  ${svgText("85%", 95, 278, 46, { fill: "#8ad8c4", weight: 800 })}
  ${svgText("17 of 20 tasks completed", 95, 320, 15, { fill: "#bac6d5" })}
  ${svgText("4.4/5", 410, 278, 46, { fill: "#8ad8c4", weight: 800 })}
  ${svgText("average usefulness", 410, 320, 15, { fill: "#bac6d5" })}
  ${svgText("80%", 725, 278, 46, { fill: "#8ad8c4", weight: 800 })}
  ${svgText("would use again", 725, 320, 15, { fill: "#bac6d5" })}
  ${svgText("65%", 1040, 278, 46, { fill: "#f6a8b7", weight: 800 })}
  ${svgText("reported a confusion point", 1040, 320, 15, { fill: "#bac6d5" })}
</g>
<rect x="70" y="390" width="610" height="390" rx="20" fill="#ffffff"/>
<rect x="700" y="390" width="630" height="390" rx="20" fill="#ffffff"/>
${svgText("Validation profile", 100, 435, 23, { weight: 800 })}
${svgText("Current prototype verification", 730, 435, 23, { weight: 800 })}
${svgText("Users", 100, 490, 15)}<rect x="230" y="474" width="350" height="16" rx="8" fill="#e8eef3"/><rect x="230" y="474" width="315" height="16" rx="8" fill="#4fb89d"/>${svgText("18", 630, 490, 15, { weight: 800 })}
${svgText("Would use again", 100, 548, 15)}<rect x="230" y="532" width="350" height="16" rx="8" fill="#e8eef3"/><rect x="230" y="532" width="280" height="16" rx="8" fill="#1789df"/>${svgText("16", 630, 548, 15, { weight: 800 })}
${svgText("Mobile/tablet", 100, 606, 15)}<rect x="230" y="590" width="350" height="16" rx="8" fill="#e8eef3"/><rect x="230" y="590" width="175" height="16" rx="8" fill="#e66f86"/>${svgText("10", 630, 606, 15, { weight: 800 })}
${svgText("Desktop/laptop", 100, 664, 15)}<rect x="230" y="648" width="350" height="16" rx="8" fill="#e8eef3"/><rect x="230" y="648" width="175" height="16" rx="8" fill="#1789df"/>${svgText("10", 630, 664, 15, { weight: 800 })}
${svgText("Check", 730, 485, 13, { fill: "#607087", weight: 800 })}
${svgText("Result", 1010, 485, 13, { fill: "#607087", weight: 800 })}
${svgText("Evidence", 1150, 485, 13, { fill: "#607087", weight: 800 })}
<path d="M730 500H1300M730 550H1300M730 600H1300M730 650H1300M730 700H1300M730 750H1300" stroke="#e6ebef"/>
${svgText("8 key pages", 730, 535, 15)}${svgText("PASS", 1010, 535, 15, { fill: "#17755f", weight: 800 })}${svgText("HTTP 200", 1150, 535, 15)}
${svgText("Tag search", 730, 585, 15)}${svgText("PASS", 1010, 585, 15, { fill: "#17755f", weight: 800 })}${svgText("5 results", 1150, 585, 15)}
${svgText("Artwork detail", 730, 635, 15)}${svgText("PASS", 1010, 635, 15, { fill: "#17755f", weight: 800 })}${svgText("A010 loaded", 1150, 635, 15)}
${svgText("Profile page", 730, 685, 15)}${svgText("PASS", 1010, 685, 15, { fill: "#17755f", weight: 800 })}${svgText("HTTP 200", 1150, 685, 15)}
${svgText("Dashboard page", 730, 735, 15)}${svgText("PASS", 1010, 735, 15, { fill: "#17755f", weight: 800 })}${svgText("HTTP 200", 1150, 735, 15)}
${svgText("Sources: data/validation-results.csv · prototype-testing-notes.md · current local-server smoke test · No new external participants claimed.", 70, 840, 14, { fill: "#8f9db0" })}
</svg>`;

await sharp(Buffer.from(evidenceSvg))
  .png()
  .toFile(path.join(screenshots, "user-testing-evidence.png"));

console.log("Lab 13 evidence images rendered.");
