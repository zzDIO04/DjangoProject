
import { useState } from "react";
import { Navigation } from "@/components/Navigation";
import { Button } from "@/components/ui/button";
import { Card, CardContent } from "@/components/ui/card";
import { toast } from "sonner";

interface Question {
  id: number;
  question: string;
  options: string[];
  correctAnswer: number;
}

const questions: Question[] = [
  {
    id: 1,
    question: "Quanto é 8 + 5?",
    options: ["12", "13", "14", "15"],
    correctAnswer: 1,
  },
  {
    id: 2,
    question: "Se você tem 3 dezenas, quantas unidades você tem?",
    options: ["3", "10", "30", "300"],
    correctAnswer: 2,
  },
  {
    id: 3,
    question: "Qual é a metade de 18?",
    options: ["7", "8", "9", "10"],
    correctAnswer: 2,
  },
];

const MathQuiz = () => {
  const [currentQuestion, setCurrentQuestion] = useState(0);
  const [score, setScore] = useState(0);
  const [showScore, setShowScore] = useState(false);

  const handleAnswerClick = (selectedAnswer: number) => {
    if (selectedAnswer === questions[currentQuestion].correctAnswer) {
      setScore(score + 1);
      toast.success("Resposta correta! 🎉");
    } else {
      toast.error("Ops! Tente novamente! 💪");
    }

    const nextQuestion = currentQuestion + 1;
    if (nextQuestion < questions.length) {
      setCurrentQuestion(nextQuestion);
    } else {
      setShowScore(true);
    }
  };

  const resetQuiz = () => {
    setCurrentQuestion(0);
    setScore(0);
    setShowScore(false);
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-purple-50 to-white">
      <Navigation />
      <main className="container mx-auto px-4 pt-24 pb-12">
        <Card className="max-w-2xl mx-auto">
          <CardContent className="p-6">
            {showScore ? (
              <div className="text-center">
                <h2 className="text-3xl font-bold mb-4">
                  Quiz Completo! 🎈
                </h2>
                <p className="text-xl mb-6">
                  Você acertou {score} de {questions.length} questões!
                </p>
                <Button onClick={resetQuiz} size="lg">
                  Tentar Novamente
                </Button>
              </div>
            ) : (
              <div>
                <div className="mb-8">
                  <p className="text-sm text-gray-500 mb-2">
                    Questão {currentQuestion + 1} de {questions.length}
                  </p>
                  <h2 className="text-2xl font-bold">
                    {questions[currentQuestion].question}
                  </h2>
                </div>
                <div className="grid grid-cols-1 md:grid-cols-2 gap-4">
                  {questions[currentQuestion].options.map((option, index) => (
                    <Button
                      key={index}
                      onClick={() => handleAnswerClick(index)}
                      variant="outline"
                      className="p-6 text-lg hover:bg-purple-50"
                    >
                      {option}
                    </Button>
                  ))}
                </div>
              </div>
            )}
          </CardContent>
        </Card>
      </main>
    </div>
  );
};

export default MathQuiz;
