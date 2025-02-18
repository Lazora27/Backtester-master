import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveTrendLine_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveTrendLine und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'AdaptiveTrendLine': {
                'class': AdaptiveTrendLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveTrendLine'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'AdaptiveTrendLine': 1.0,
            'HilbertTrendline': 1.0
        })
    )
