import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
