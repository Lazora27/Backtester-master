import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'CumulativeTick': 1.0
        })
    )
