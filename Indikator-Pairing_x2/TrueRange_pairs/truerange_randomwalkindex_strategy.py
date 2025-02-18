import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
