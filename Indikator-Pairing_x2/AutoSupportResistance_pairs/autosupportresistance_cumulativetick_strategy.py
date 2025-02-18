import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'CumulativeTick': 1.0
        })
    )
