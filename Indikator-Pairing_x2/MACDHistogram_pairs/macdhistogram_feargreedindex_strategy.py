import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_FearGreedIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und FearGreedIndex
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'FearGreedIndex': 1.0
        })
    )
