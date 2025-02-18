import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'CumulativeTick': 1.0
        })
    )
