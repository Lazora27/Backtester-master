import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RandomWalkIndex_OpenInterest_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RandomWalkIndex und OpenInterest
    """
    
    params = (
        ('indicators', {
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            },
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            }
        }),
        ('weights', {
            'RandomWalkIndex': 1.0,
            'OpenInterest': 1.0
        })
    )
