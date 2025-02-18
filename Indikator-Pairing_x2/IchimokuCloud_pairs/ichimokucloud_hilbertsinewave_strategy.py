import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'HilbertSinewave': 1.0
        })
    )
