import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'HilbertSinewave': 1.0
        })
    )
