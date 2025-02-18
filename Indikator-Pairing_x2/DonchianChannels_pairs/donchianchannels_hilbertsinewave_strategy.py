import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianChannels_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianChannels und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'DonchianChannels': 1.0,
            'HilbertSinewave': 1.0
        })
    )
