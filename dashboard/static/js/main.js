document.addEventListener("DOMContentLoaded", () => {
    const toolSelector = document.getElementById("tool-selector");
    
    // Only run if on playground page
    if (toolSelector) {
        const dynamicForm = document.getElementById("dynamic-form");
        const runBtn = document.getElementById("run-btn");
        const outputBlock = document.getElementById("output-block");
        const execTime = document.getElementById("exec-time");
        const execStatus = document.getElementById("exec-status");
        const metricsBar = document.getElementById("metrics-bar");
        const loadingSpinner = document.getElementById("loading-spinner");
        const copyBtn = document.getElementById("copy-btn");

        // Tool arguments mapping (lightweight client-side registry)
        const toolArgs = {
            "math/add": [{name: "a", type: "number", label: "Value A"}, {name: "b", type: "number", label: "Value B"}],
            "math/factorial": [{name: "n", type: "number", label: "Integer N"}],
            "math/is_prime": [{name: "n", type: "number", label: "Integer N"}],
            "math/fibonacci": [{name: "n", type: "number", label: "Integer N"}],
            "math/gcd": [{name: "a", type: "number", label: "Value A"}, {name: "b", type: "number", label: "Value B"}],
            "math/lcm": [{name: "a", type: "number", label: "Value A"}, {name: "b", type: "number", label: "Value B"}],
            "string/reverse": [{name: "text", type: "text", label: "String to Reverse"}],
            "string/palindrome": [{name: "text", type: "text", label: "Text"}],
            "string/word_count": [{name: "text", type: "text", label: "Text Content"}],
            "random/generate_password": [{name: "length", type: "number", label: "Length (e.g. 16)"}],
            "random/random_int": [{name: "min_val", type: "number", label: "Min Value"}, {name: "max_val", type: "number", label: "Max Value"}]
        };

        toolSelector.addEventListener("change", (e) => {
            const toolId = e.target.value;
            const args = toolArgs[toolId];
            
            dynamicForm.innerHTML = '<h3>2. Configure Parameters</h3>';
            args.forEach(arg => {
                const group = document.createElement("div");
                group.className = "form-group";
                group.innerHTML = `
                    <label>${arg.label}</label>
                    <input type="${arg.type}" name="${arg.name}" class="glass-input arg-input" required />
                `;
                dynamicForm.appendChild(group);
            });
            
            dynamicForm.classList.remove("hidden");
            runBtn.classList.remove("hidden");
        });

        runBtn.addEventListener("click", async () => {
            const toolId = toolSelector.value;
            const inputs = document.querySelectorAll(".arg-input");
            let payload = {};
            
            inputs.forEach(input => {
                let val = input.value;
                if(input.type === 'number') val = Number(val);
                payload[input.name] = val;
            });

            // UI Loading state
            outputBlock.innerText = "";
            loadingSpinner.classList.remove("hidden");
            metricsBar.classList.add("hidden");
            copyBtn.classList.add("hidden");

            try {
                const response = await fetch("/api/run-tool", {
                    method: "POST",
                    headers: {"Content-Type": "application/json"},
                    body: JSON.stringify({ tool_id: toolId, payload: payload })
                });

                const data = await response.json();
                
                loadingSpinner.classList.add("hidden");
                metricsBar.classList.remove("hidden");
                
                if (data.success) {
                    outputBlock.innerText = typeof data.result === 'object' ? JSON.stringify(data.result, null, 2) : data.result;
                    outputBlock.style.color = "var(--text-color)";
                    execTime.innerText = data.execution_time_ms;
                    execStatus.innerText = "OK ✔️";
                    execStatus.style.color = "var(--success)";
                    copyBtn.classList.remove("hidden");
                } else {
                    outputBlock.innerText = `Error: ${data.error}`;
                    outputBlock.style.color = "var(--error)";
                    execTime.innerText = "0.00";
                    execStatus.innerText = "FAIL ❌";
                    execStatus.style.color = "var(--error)";
                }
            } catch (error) {
                loadingSpinner.classList.add("hidden");
                outputBlock.innerText = `Network Error: ${error}`;
            }
        });
        
        copyBtn.addEventListener("click", () => {
            navigator.clipboard.writeText(outputBlock.innerText);
            copyBtn.innerText = "Copied!";
            setTimeout(() => { copyBtn.innerText = "Copy"; }, 2000);
        });
    }
});