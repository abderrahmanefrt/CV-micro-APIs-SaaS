interface Props {
  apiKey: string;
}

function TestService({ apiKey }: Props) {
  const [file, setFile] = useState<File | null>(null);
  const [resultat, setResultat] = useState<string | null>(null);

  const handleTest = async () => {
    // à toi de compléter
  };

  return (
    // à toi de compléter : input file + bouton + affichage résultat
  );
}

export default TestService;
