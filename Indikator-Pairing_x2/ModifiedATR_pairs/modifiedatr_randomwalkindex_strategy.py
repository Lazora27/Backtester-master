import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
