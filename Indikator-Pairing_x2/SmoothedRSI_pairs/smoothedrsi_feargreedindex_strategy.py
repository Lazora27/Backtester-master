import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'FearGreedIndex': 1.0
        })
    )
