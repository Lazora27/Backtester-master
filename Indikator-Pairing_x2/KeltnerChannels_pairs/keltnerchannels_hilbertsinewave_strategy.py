import backtrader as bt
from ..base_strategy import FlexibleStrategy

class KeltnerChannels_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von KeltnerChannels und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'KeltnerChannels': {
                'class': KeltnerChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerChannels'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'KeltnerChannels': 1.0,
            'HilbertSinewave': 1.0
        })
    )
