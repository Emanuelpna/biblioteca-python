import uuid


class CodeGenerator:
    @staticmethod
    def getUniqueCode():
        uniqueID = str(uuid.uuid4())

        uniqueIDParts = uniqueID.split('-')

        return uniqueIDParts[0]
