import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'HilbertTrendline': 1.0
        })
    )
