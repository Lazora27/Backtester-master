import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'AdaptiveATR': 1.0
        })
    )
