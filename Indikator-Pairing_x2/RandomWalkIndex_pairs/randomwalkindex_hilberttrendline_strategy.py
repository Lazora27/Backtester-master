import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RandomWalkIndex_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RandomWalkIndex und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'RandomWalkIndex': {
                'class': RandomWalkIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RandomWalkIndex'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'RandomWalkIndex': 1.0,
            'HilbertTrendline': 1.0
        })
    )
