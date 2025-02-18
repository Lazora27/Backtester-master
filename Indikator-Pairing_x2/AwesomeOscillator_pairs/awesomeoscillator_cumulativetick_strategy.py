import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'CumulativeTick': 1.0
        })
    )
