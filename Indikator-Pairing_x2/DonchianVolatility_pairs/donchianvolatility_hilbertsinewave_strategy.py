import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'HilbertSinewave': 1.0
        })
    )
