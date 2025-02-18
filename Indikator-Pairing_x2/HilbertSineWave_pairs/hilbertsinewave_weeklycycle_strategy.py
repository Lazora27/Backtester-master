import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HilbertSinewave_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HilbertSinewave und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'HilbertSinewave': {
                'class': HilbertSinewave,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertSinewave'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'HilbertSinewave': 1.0,
            'WeeklyCycle': 1.0
        })
    )
