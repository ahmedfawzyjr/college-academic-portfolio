"""
Distributed Academic Task & Queue Engine
Implements Thread-Safe Priority Queue & Task Processor.
"""

import heapq
import threading
import time
from typing import Dict, Any, Optional

class PrioritizedTask:
    def __init__(self, priority: int, task_id: str, payload: Dict[str, Any]):
        self.priority = priority  # Higher priority executes first
        self.task_id = task_id
        self.payload = payload
        self.created_at = time.time()

    def __lt__(self, other: 'PrioritizedTask') -> bool:
        # Invert priority for max-heap behavior via heapq
        return self.priority > other.priority

class AcademicTaskEngine:
    def __init__(self):
        self._heap = []
        self._lock = threading.Lock()
        self._processed = {}

    def submit_task(self, task_id: str, priority: int, payload: Dict[str, Any]):
        with self._lock:
            task = PrioritizedTask(priority, task_id, payload)
            heapq.heappush(self._heap, task)

    def process_next(self) -> Optional[Dict[str, Any]]:
        with self._lock:
            if not self._heap:
                return None
            task: PrioritizedTask = heapq.heappop(self._heap)
        
        # Execute task logic
        result = {
            "task_id": task.task_id,
            "status": "COMPLETED",
            "executed_priority": task.priority,
            "output": f"Processed payload for {task.payload.get('action')}"
        }
        self._processed[task.task_id] = result
        return result

    def get_queue_size(self) -> int:
        with self._lock:
            return len(self._heap)
