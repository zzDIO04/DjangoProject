
import { UserRound } from "lucide-react";
import { Button } from "@/components/ui/button";
import { Link } from "react-router-dom";

export const Navigation = () => {
  return (
    <nav className="w-full px-4 py-4 flex justify-between items-center bg-white/80 backdrop-blur-sm fixed top-0 z-50">
      <Link to="/" className="text-2xl font-bold font-nunito text-quiz-math">
        QuizKids
      </Link>
      <Link to="/teacher">
        <Button variant="outline" size="sm" className="flex items-center gap-2">
          <UserRound className="h-4 w-4" />
          Painel do Professor
        </Button>
      </Link>
    </nav>
  );
};
