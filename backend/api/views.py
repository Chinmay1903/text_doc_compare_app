from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.parsers import MultiPartParser
from .extract_text import extract_text_from_file
from .similarity import compute_pairwise_similarity

class MultiDocumentSimilarity(APIView):
    parser_classes = [MultiPartParser]

    def post(self, request):
        files = request.FILES.getlist("files")
        if len(files) < 2:
            return Response({"error": "Upload at least two files."}, status=400)

        texts, names = [], []
        for f in files:
            text = extract_text_from_file(f)
            if text.strip():
                texts.append(text)
                names.append(f.name)

        if len(texts) < 2:
            return Response({"error": "Not enough valid text to compare."}, status=400)

        sim_matrix = compute_pairwise_similarity(texts)

        # Create pairwise results
        results = []
        for i in range(len(names)):
            for j in range(i + 1, len(names)):  # avoid same and duplicate
                results.append({
                    "pair": f"{names[i]} - {names[j]}",
                    "score": round(sim_matrix[i][j], 4)
                })

        return Response({"results": results})
