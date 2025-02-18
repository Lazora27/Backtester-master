import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
