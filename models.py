"""
Temporal First Design Data Models
All entities exist as time-ordered event streams with validation
Architecture Choice: Pydantic models ensure type safety and runtime validation
while maintaining compatibility with Firestore's document structure
"""
from datetime import datetime, timezone
from typing import Dict, Any, List, Optional, Union
from enum import Enum
from uuid import uuid4
from pydantic import BaseModel, Field, validator, root_validator
import structlog

logger = structlog.get_logger()

class NodeType(Enum):
    """Types of nodes in the reality-graph"""
    PHYSICAL_OBJECT = "physical_object"
    DATA_PACKET = "data_packet"
    TRANSPORT_VEHICLE = "transport_vehicle"
    COMPUTE_NODE = "compute_node"
    STORAGE_NODE = "storage_node"

class CapabilityType(Enum):
    """Types of capabilities for resource negotiation"""
    READ = "read"
    WRITE = "write"
    EXEC