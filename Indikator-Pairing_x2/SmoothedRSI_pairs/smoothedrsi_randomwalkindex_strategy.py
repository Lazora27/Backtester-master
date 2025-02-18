import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_RandomWalkIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und RandomWalkIndex
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'RandomWalkIndex': 1.0
        })
    )
