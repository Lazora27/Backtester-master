import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
