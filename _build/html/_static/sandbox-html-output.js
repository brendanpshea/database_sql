document.addEventListener("DOMContentLoaded", () => {
  const htmlOutputs = document.querySelectorAll(".output.text_html");

  htmlOutputs.forEach((output, index) => {
    if (output.dataset.sandboxed === "true") {
      return;
    }

    const html = output.innerHTML.trim();

    if (!/(<!DOCTYPE html|<html[\s>]|<head[\s>]|<body[\s>]|<style[\s>]|<script[\s>])/i.test(html)) {
      return;
    }

    const iframe = document.createElement("iframe");
    iframe.className = "sandboxed-html-output";
    iframe.setAttribute(
      "sandbox",
      "allow-scripts allow-same-origin allow-forms allow-popups"
    );
    iframe.setAttribute("loading", index < 2 ? "eager" : "lazy");
    iframe.setAttribute("title", `Interactive notebook content ${index + 1}`);

    const resizeFrame = () => {
      try {
        const documentElement = iframe.contentDocument?.documentElement;
        const body = iframe.contentDocument?.body;

        if (!documentElement || !body) {
          return;
        }

        const nextHeight = Math.max(
          documentElement.scrollHeight,
          body.scrollHeight,
          body.offsetHeight,
          360
        );

        iframe.style.height = `${nextHeight + 8}px`;
      } catch {
        // Ignore resize failures for sandboxed or third-party embedded content.
      }
    };

    iframe.addEventListener("load", () => {
      resizeFrame();
      setTimeout(resizeFrame, 150);
      setTimeout(resizeFrame, 750);

      try {
        const body = iframe.contentDocument?.body;
        if (body && "ResizeObserver" in window) {
          const observer = new ResizeObserver(() => resizeFrame());
          observer.observe(body);
        }
      } catch {
        // Ignore observer setup failures.
      }
    });

    iframe.srcdoc = html;
    output.replaceChildren(iframe);
    output.classList.add("output--sandboxed");
    output.dataset.sandboxed = "true";
  });
});
