const processBtn =
    document.getElementById("process-btn");

const sendBtn =
    document.getElementById("send-btn");


// PROCESS VIDEO
processBtn.addEventListener(
    "click",
    async () => {

        const youtubeInput =
            document.getElementById(
                "youtube-url"
            );

        const youtubeUrl =
            youtubeInput.value.trim();

        const chatContainer =
            document.getElementById(
                "chat-container"
            );

        if (!youtubeUrl) {
            return;
        }

        processBtn.disabled = true;

        processBtn.innerText =
            "Processing...";

        try {

            const response =
                await fetch(
                    "/process-video",
                    {
                        method: "POST",

                        headers: {
                            "Content-Type":
                                "application/json"
                        },

                        body: JSON.stringify({
                            url: youtubeUrl
                        })
                    }
                );

            const data =
                await response.json();

            console.log(data);

            // SUCCESS
            if (data.success) {

                // Update status
                const videoStatus =
                    document.getElementById(
                        "video-status"
                    );

                videoStatus.textContent =
                    "✅ Video ready to chat";

                // Show input
                const inputSection =
                    document.getElementById(
                        "input-section"
                    );

                inputSection.style.display =
                    "flex";

                // AI Message
                const messageDiv =
                    document.createElement(
                        "div"
                    );

                messageDiv.classList.add(
                    "message",
                    "ai-message"
                );

                messageDiv.textContent =
                    data.message;

                chatContainer.appendChild(
                    messageDiv
                );
            }

            // ERROR
            else {

                const errorDiv =
                    document.createElement(
                        "div"
                    );

                errorDiv.classList.add(
                    "message",
                    "ai-message"
                );

                errorDiv.textContent =
                    `❌ ${data.message}`;

                chatContainer.appendChild(
                    errorDiv
                );
            }

            youtubeInput.value = "";

            chatContainer.scrollTop =
                chatContainer.scrollHeight;

        } catch (error) {

            console.log(error);

        } finally {

            processBtn.disabled = false;

            processBtn.innerText =
                "Process Video";
        }
    }
);

const questionInput =
    document.getElementById(
        "question-input"
    );

// ENTER TO SEND
questionInput.addEventListener(
    "keydown",
    (event) => {

        if (
            event.key === "Enter"
            &&
            !event.shiftKey
        ) {

            event.preventDefault();

            sendBtn.click();
        }
    }
);


// CHAT BUTTON
sendBtn.addEventListener(
    "click",
    async () => {

        const questionInput =
            document.getElementById(
                "question-input"
            );

        const question =
            questionInput.value.trim();

        const chatContainer =
            document.getElementById(
                "chat-container"
            );

        if (!question) {
            return;
        }

        // USER MESSAGE
        const userMessage =
            document.createElement(
                "div"
            );

        userMessage.classList.add(
            "message",
            "user-message"
        );

        userMessage.textContent =
            question;

        chatContainer.appendChild(
            userMessage
        );

        // AI THINKING MESSAGE
        const aiMessage =
            document.createElement(
                "div"
            );

        aiMessage.classList.add(
            "message",
            "ai-message"
        );

        aiMessage.textContent =
            "Thinking...";

        chatContainer.appendChild(
            aiMessage
        );

        // CLEAR INPUT
        questionInput.value = "";

        // AUTO SCROLL
        chatContainer.scrollTop =
            chatContainer.scrollHeight;

        try {
            console.log(question);

            // SEND QUESTION
            const response =
                await fetch("/ask", {

                    method: "POST",

                    headers: {
                        "Content-Type":
                            "application/json"
                    },

                    body: JSON.stringify({

                        question: question
                    })
                });

            const data =
                await response.json();

            console.log(data);

            // SHOW ANSWER
            if (data.success) {

                aiMessage.textContent =
                    data.answer;

            } else {

                aiMessage.textContent =
                    `❌ ${data.message}`;
            }

        } catch (error) {

            console.log(error);

            aiMessage.textContent =
                "❌ Something went wrong";
        }

        // AUTO SCROLL
        chatContainer.scrollTop =
            chatContainer.scrollHeight;
    }
);