
import { Calculator, Atom, Book } from "lucide-react";
import { Navigation } from "@/components/Navigation";
import { SubjectCard } from "@/components/SubjectCard";

const subjects = [
  {
    title: "Matemática",
    description: "Descubra como os números podem ser divertidos!",
    icon: Calculator,
    color: "text-quiz-math",
    bgColor: "bg-purple-100",
    path: "/quiz/math",
  },
  {
    title: "Ciências",
    description: "Explore o incrível mundo da ciência!",
    icon: Atom,
    color: "text-quiz-science",
    bgColor: "bg-blue-100",
    path: "/quiz/science",
  },
  {
    title: "História",
    description: "Viaje no tempo e conheça histórias fascinantes!",
    icon: Book,
    color: "text-quiz-history",
    bgColor: "bg-orange-100",
    path: "/quiz/history",
  },
];

const Index = () => {
  return (
    <div className="min-h-screen bg-gradient-to-b from-blue-50 to-white font-nunito">
      <Navigation />
      <main className="container mx-auto px-4 pt-24 pb-12">
        <div className="text-center mb-12">
          <h1 className="text-4xl md:text-5xl font-bold mb-4 text-gray-800">
            Escolha seu Desafio!
          </h1>
          <p className="text-xl text-gray-600">
            Aprenda brincando com nossos quizzes.
          </p>
        </div>
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8 justify-items-center">
          {subjects.map((subject) => (
            <SubjectCard key={subject.title} {...subject} />
          ))}
        </div>
      </main>
    </div>
  );
};

export default Index;
