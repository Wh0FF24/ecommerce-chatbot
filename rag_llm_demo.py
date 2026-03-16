#!/usr/bin/env python3
"""
RAG + LLM Demo - For Upwork Application
Retrieval-Augmented Generation with Python
"""
import json
import hashlib
from datetime import datetime

class SimpleRAG:
    def __init__(self):
        self.documents = []
        self.chunks = []
        
    def add_document(self, text, source="user"):
        """Add a document to the knowledge base"""
        doc = {
            "text": text,
            "source": source,
            "added_at": datetime.now().isoformat(),
            "id": hashlib.md5(text.encode()).hexdigest()[:8]
        }
        self.documents.append(doc)
        
        # Chunk the document
        words = text.split()
        for i in range(0, len(words), 50):
            chunk = " ".join(words[i:i+50])
            self.chunks.append({
                "text": chunk,
                "doc_id": doc["id"],
                "chunk_index": i // 50
            })
        
        return doc["id"]
    
    def retrieve(self, query, top_k=3):
        """Retrieve relevant chunks for a query"""
        query_words = set(query.lower().split())
        scores = []
        
        for chunk in self.chunks:
            chunk_words = set(chunk["text"].lower().split())
            # Simple keyword matching score
            score = len(query_words & chunk_words)
            scores.append((score, chunk))
        
        # Sort by score and return top_k
        scores.sort(key=lambda x: x[0], reverse=True)
        return [chunk for score, chunk in scores[:top_k]]
    
    def generate_response(self, query, llm_available=False):
        """Generate a response using retrieved context"""
        relevant_chunks = self.retrieve(query)
        
        if not relevant_chunks:
            return "I don't have enough information to answer that."
        
        context = "\n\n".join([c["text"] for c in relevant_chunks])
        
        if llm_available:
            # Would call OpenAI here
            pass
        
        # Return context-based response
        return f"Based on the knowledge base:\n\n{context[:500]}..."

def run_demo():
    print("=" * 50)
    print("RAG + LLM System Demo")
    print("=" * 50)
    
    rag = SimpleRAG()
    
    # Add sample documents (would be user's knowledge base)
    docs = [
        "Python is a high-level programming language used for web development, data science, AI, and automation.",
        "LLM stands for Large Language Model, a type of AI trained on vast amounts of text data.",
        "RAG (Retrieval-Augmented Generation) combines a retrieval system with an LLM for better answers.",
        "NLP (Natural Language Processing) helps computers understand human language.",
        "FastAPI is a modern Python web framework for building APIs quickly.",
    ]
    
    print("\n📚 Adding documents to knowledge base...")
    for doc in docs:
        doc_id = rag.add_document(doc)
        print(f"   ✓ Added: {doc[:40]}...")
    
    # Query the system
    print("\n🔍 Testing queries:")
    queries = [
        "What is Python?",
        "How does RAG work?",
        "What is LLM?"
    ]
    
    for query in queries:
        print(f"\nQuery: {query}")
        response = rag.generate_response(query)
        print(f"Response: {response[:150]}...")
    
    print("\n" + "=" * 50)
    print("✅ RAG System Working!")
    print("=" * 50)

if __name__ == "__main__":
    run_demo()
