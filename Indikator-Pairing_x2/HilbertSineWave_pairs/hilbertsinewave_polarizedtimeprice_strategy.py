import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertSinewave_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertSinewave und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'HilbertSinewave': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
