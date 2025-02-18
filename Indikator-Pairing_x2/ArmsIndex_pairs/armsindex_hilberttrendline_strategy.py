import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'HilbertTrendline': 1.0
        })
    )
