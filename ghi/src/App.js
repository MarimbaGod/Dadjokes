import { useEffect, useState } from "react";
import Construct from "./Construct.js";
import ErrorNotification from "./ErrorNotification";
import "./App.css";
import { Button, useColorMode, VStack, Text } from '@chakra-ui/react';

function App() {
  const [joke, setJoke] = useState('');
  const { colorMode, toggleColorMode } = useColorMode();

  const fetchJoke = async () => {
    try {
      const response = await fetch("http://localhost:8000/api/joke");
      if (!response.ok) {
        throw new Error("Network response error")
      }
      const data = await response.json();
      setJoke(data.joke);
    } catch (error) {
      console.error("Error fetching joke:", error);
    }
  };

  return (
    <VStack spacing={4}>
      <Button
        size="lg"
        colorScheme="blue"
        onClick={fetchJoke}
      >
        Tell me a Dad Joke!
      </Button>
      {joke && <Text fontSize="xl">{joke}</Text>}
      <Button onClick={toggleColorMode}>
        Toggle {colorMode === "light" ? "Dark" : "Light"}
      </Button>
    </VStack>
  );
}

export default App;
