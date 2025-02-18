import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertSinewave_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertSinewave und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'HilbertSinewave': 1.0,
            'HilbertTrendline': 1.0
        })
    )
