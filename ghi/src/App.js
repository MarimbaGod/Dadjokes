import { useState } from "react";
import "./App.css";
import { Button, useColorMode, VStack, Text, Box, Flex } from '@chakra-ui/react';
import { useSpring, animated } from '@react-spring/web';

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

  const fade = useSpring({
    opacity: joke ? 1 : 0,
    transform: joke ? 'translateY(0)' : 'translateY(-20px)',
    config: { duration: 500 },
  });

  return (
    <Flex direction="column" align="center" justify="center" minH="100vh">
      <VStack spacing={4}>
        <Button
          size="lg"
          colorScheme="blue"
          onClick={fetchJoke}
        >
          Tell me a Dad Joke!
        </Button>
        <animated.div style={fade}>
          {joke && <Box p={5} shadow="md" borderWidth="1px" borderRadius="md">
            <Text fontSize="xl" color={colorMode === 'light' ? 'blue.600' : 'orange.300'}>
              {joke}
            </Text>
          </Box>}
          </animated.div>
          <Button onClick={toggleColorMode}>
            Toggle {colorMode === "light" ? "Dark" : "Light"}
          </Button>
      </VStack>
    </Flex>
  );
}

export default App;
