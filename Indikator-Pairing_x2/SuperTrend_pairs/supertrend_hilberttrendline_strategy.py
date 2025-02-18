import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperTrend_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperTrend und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'SuperTrend': 1.0,
            'HilbertTrendline': 1.0
        })
    )
