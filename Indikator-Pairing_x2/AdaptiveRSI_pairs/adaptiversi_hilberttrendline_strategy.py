import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'HilbertTrendline': 1.0
        })
    )
