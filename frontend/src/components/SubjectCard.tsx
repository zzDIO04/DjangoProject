
import { LucideIcon } from "lucide-react";
import { Button } from "@/components/ui/button";
import { toast } from "sonner";
import { useNavigate } from "react-router-dom";

interface SubjectCardProps {
  title: string;
  description: string;
  icon: LucideIcon;
  color: string;
  bgColor: string;
  path: string;
}

export const SubjectCard = ({
  title,
  description,
  icon: Icon,
  color,
  bgColor,
  path,
}: SubjectCardProps) => {
  const navigate = useNavigate();

  const handleStart = () => {
    toast.success(`Iniciando o quiz de ${title}!`);
    navigate(path);
  };

  return (
    <div
      className={`p-6 rounded-xl shadow-lg transition-all duration-300 hover:animate-card-hover ${bgColor} max-w-sm w-full`}
    >
      <div className="flex flex-col items-center text-center gap-4">
        <Icon className={`w-16 h-16 ${color}`} />
        <h3 className="text-xl font-bold font-nunito">{title}</h3>
        <p className="text-gray-700">{description}</p>
        <Button
          onClick={handleStart}
          className="mt-4 bg-white hover:bg-gray-50 text-gray-800"
        >
          Começar
        </Button>
      </div>
    </div>
  );
};
