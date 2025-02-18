import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
