import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und BarStrength
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'BarStrength': 1.0
        })
    )
