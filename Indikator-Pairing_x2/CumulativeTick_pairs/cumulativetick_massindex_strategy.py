import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und MassIndex
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'MassIndex': 1.0
        })
    )
