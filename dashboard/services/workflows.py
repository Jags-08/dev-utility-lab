from typing import List, Dict, Any
from dashboard.services.dispatcher import dispatch_tool

class WorkflowEngine:
    def __init__(self) -> None:
        self.history: List[Dict[str, Any]] = []

    def execute_pipeline(self, steps: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Executes a sequence of utilities, piping the output of one into the input of the next.
        """
        context: Any = None
        results = []
        
        for index, step in enumerate(steps):
            tool_id = step.get("tool_id")
            payload = step.get("payload", {})
            
            if context is not None and step.get("pipe"):
                # Inject output from previous step if piped
                pipe_key = step.get("pipe_key", "data")
                payload[pipe_key] = context
            
            if not tool_id:
                return {"success": False, "error": f"Missing tool_id at step {index}"}
                
            res = dispatch_tool(tool_id, payload)
            if not res.get("success"):
                return {"success": False, "error": f"Workflow failed at index {index}", "details": res}
            
            context = res.get("result")
            results.append({"step": index, "tool": tool_id, "output": context})
        
        return {"success": True, "results": results, "final_output": context}
