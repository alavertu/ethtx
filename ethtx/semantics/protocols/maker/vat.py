#  Copyright 2021 DAI Foundation
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at: http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.

from ethtx.models.semantics_model import TransformationSemantics
from ethtx.semantics.base import Base


class Vat(Base):
    code_hash = "0x808b98f6475736d56c978e4fb476175ecd9d7abdab0797017fc10c7f46311a59"
    contract_semantics = dict(
        transformations={
            "0x2424be5c": {  # urns
                "art": TransformationSemantics(transformation="art"),
                "ilk": TransformationSemantics(
                    transformed_type="string", transformation="string_from_bytes(ilk)"
                ),
            },
            "ink": TransformationSemantics(transformation="ink"),
            "0x3b663195": {  # init
                "ilk": TransformationSemantics(
                    transformed_type="string", transformation="string_from_bytes(ilk)"
                )
            },
            "0x6111be2e": {  # flux
                "ilk": TransformationSemantics(
                    transformed_type="string", transformation="string_from_bytes(ilk)"
                ),
                "wad": TransformationSemantics(transformation="wad"),
            },
            "0x7cdd3fde": {  # slip
                "ilk": TransformationSemantics(
                    transformed_type="string", transformation="string_from_bytes(ilk)"
                ),
                "wad": TransformationSemantics(transformation="wad"),
            },
            "0x76088703": {  # frob
                "dart": TransformationSemantics(transformation="dart"),
                "dink": TransformationSemantics(transformation="dink"),
                "i": TransformationSemantics(
                    transformed_type="string", transformation="string_from_bytes(i)"
                ),
            },
            "0x870c616d": {  # fork
                "dart": TransformationSemantics(transformation="dart"),
                "dink": TransformationSemantics(transformation="dink"),
                "i": TransformationSemantics(
                    transformed_type="string", transformation="string_from_bytes(i)"
                ),
            },
            "0xb65337df": {  # fold
                "i": TransformationSemantics(
                    transformed_type="string", transformation="string_from_bytes(i)"
                ),
                "rate": TransformationSemantics(transformation="rate"),
            },
            "0xbb35783b": {  # move
                "rad": TransformationSemantics(transformation="rad")
            },
            "0xd9638d36": {  # ilks
                "__input0__": TransformationSemantics(
                    transformed_type="string",
                    transformation="string_from_bytes(__input0__)",
                ),
                "Art": TransformationSemantics(transformation="Art"),
                "dust": TransformationSemantics(transformation="dust"),
                "line": TransformationSemantics(transformation="line"),
                "rate": TransformationSemantics(transformation="rate"),
                "spot": TransformationSemantics(transformation="spot"),
            },
        }
    )
