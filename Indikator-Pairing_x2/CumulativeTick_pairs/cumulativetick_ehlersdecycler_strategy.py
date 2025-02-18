import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'EhlersDecycler': 1.0
        })
    )
