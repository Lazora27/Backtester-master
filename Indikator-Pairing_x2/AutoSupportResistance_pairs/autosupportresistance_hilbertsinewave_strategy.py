import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_HilbertSinewave_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und HilbertSinewave
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'HilbertSinewave': 1.0
        })
    )
