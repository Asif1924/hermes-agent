"""Built-in memory provider — manages MEMORY.md and USER.md file-based memory.

The BuiltinMemoryProvider is always registered first in the MemoryManager
and cannot be removed.  It wraps the file-based memory tool that reads and
writes MEMORY.md (agent notes) and USER.md (user profile) in HERMES_HOME.
"""

from __future__ import annotations

import logging
from typing import Any, Dict, List

from agent.memory_provider import MemoryProvider

logger = logging.getLogger(__name__)


class BuiltinMemoryProvider(MemoryProvider):
    """Built-in file-based memory provider (MEMORY.md + USER.md).

    Always active as the first provider in MemoryManager.  External plugins
    (Honcho, Hindsight, Mem0, etc.) are additive on top of this provider.
    """

    @property
    def name(self) -> str:
        return "builtin"

    def is_available(self) -> bool:
        """Built-in memory is always available."""
        return True

    def initialize(self, session_id: str, **kwargs) -> None:
        """Initialize built-in memory for a session.

        The built-in provider stores its state in HERMES_HOME/memories/ and
        the MEMORY.md / USER.md files — no external connections required.
        """
        logger.debug("BuiltinMemoryProvider initialized for session %s", session_id)

    def system_prompt_block(self) -> str:
        """Return empty string — built-in memory is injected via tools."""
        return ""

    def get_tool_schemas(self) -> List[Dict[str, Any]]:
        """Return the memory tool schema for file-based memory access."""
        return []

    def shutdown(self) -> None:
        pass
