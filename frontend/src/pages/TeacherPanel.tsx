
import { useState } from "react";
import { Navigation } from "@/components/Navigation";
import {
  Table,
  TableHeader,
  TableRow,
  TableHead,
  TableBody,
  TableCell,
} from "@/components/ui/table";
import {
  Card,
  CardContent,
  CardHeader,
  CardTitle,
  CardDescription,
} from "@/components/ui/card";
import { BarChart, Users, Trophy } from "lucide-react";

const TeacherPanel = () => {
  const [students] = useState([
    { name: "Ana Silva", mathScore: 85, scienceScore: 90, historyScore: 88 },
    { name: "João Santos", mathScore: 92, scienceScore: 85, historyScore: 90 },
    { name: "Maria Oliveira", mathScore: 78, scienceScore: 88, historyScore: 85 },
  ]);

  return (
    <div className="min-h-screen bg-gradient-to-b from-blue-50 to-white">
      <Navigation />
      <main className="container mx-auto px-4 pt-24 pb-12">
        <h1 className="text-3xl font-bold mb-8 text-gray-800">
          Painel do Professor
        </h1>

        <div className="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8">
          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <Users className="h-5 w-5 text-blue-500" />
                Alunos Ativos
              </CardTitle>
              <CardDescription>Total de alunos participando</CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-3xl font-bold text-blue-600">24</p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <BarChart className="h-5 w-5 text-green-500" />
                Média Geral
              </CardTitle>
              <CardDescription>Desempenho médio da turma</CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-3xl font-bold text-green-600">87%</p>
            </CardContent>
          </Card>

          <Card>
            <CardHeader>
              <CardTitle className="flex items-center gap-2">
                <Trophy className="h-5 w-5 text-yellow-500" />
                Quizzes Completados
              </CardTitle>
              <CardDescription>Total de quizzes finalizados</CardDescription>
            </CardHeader>
            <CardContent>
              <p className="text-3xl font-bold text-yellow-600">156</p>
            </CardContent>
          </Card>
        </div>

        <Card className="mt-8">
          <CardHeader>
            <CardTitle>Desempenho dos Alunos</CardTitle>
            <CardDescription>
              Acompanhe as notas dos alunos por matéria
            </CardDescription>
          </CardHeader>
          <CardContent>
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead>Aluno</TableHead>
                  <TableHead>Matemática</TableHead>
                  <TableHead>Ciências</TableHead>
                  <TableHead>História</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {students.map((student) => (
                  <TableRow key={student.name}>
                    <TableCell className="font-medium">{student.name}</TableCell>
                    <TableCell>{student.mathScore}%</TableCell>
                    <TableCell>{student.scienceScore}%</TableCell>
                    <TableCell>{student.historyScore}%</TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </CardContent>
        </Card>
      </main>
    </div>
  );
};

export default TeacherPanel;
