import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'HilbertSinewave': 1.0
        })
    )
