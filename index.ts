import { CopilotClient, approveAll } from "@github/copilot-sdk";

const prompt = "In one sentence, what's an AI Agent?";

// TODO: Instantiate the CopilotClient
const client = new CopilotClient();

// TODO: Open a try/finally block to guarantee clean up
try {
  // TODO: Inside try, create a session and await session.sendAndWait("What is an AI agent?")
  const session = await client.createSession({ onPermissionRequest: approveAll });
  const response = await session.sendAndWait(prompt);

  // TODO: Print the response content using response?.data.content
  console.log(response?.data.content ?? "No response received");
} finally {
  // TODO: Inside finally, await client.stop() to close the client connection
  await client.stop();
}
