import shutil

from fastapi import (APIRouter, UploadFile, File)

from app.documents.document_service import (DocumentService)

from app.documents.document_models import (UploadResponse)


router = APIRouter(prefix="/documents", tags=["Documents"])

document_service = (DocumentService())


@router.post("/upload", response_model=UploadResponse)

async def upload_document(file: UploadFile = File(...)):

    file_path = (f"uploads/{file.filename}")

    with open(file_path, "wb") as buffer:

        shutil.copyfileobj(file.file, buffer)

    chunk_count = (document_service.ingest_pdf(file_path))

    return UploadResponse(filename=file.filename, chunks_created=chunk_count)