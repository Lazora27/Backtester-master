import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoFibonacci_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoFibonacci und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'AutoFibonacci': {
                'class': AutoFibonacci,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoFibonacci'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'AutoFibonacci': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
