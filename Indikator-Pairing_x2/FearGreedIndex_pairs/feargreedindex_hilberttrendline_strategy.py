import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FearGreedIndex_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FearGreedIndex und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'FearGreedIndex': {
                'class': FearGreedIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FearGreedIndex'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'FearGreedIndex': 1.0,
            'HilbertTrendline': 1.0
        })
    )
