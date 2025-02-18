import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_HerrickPayoffIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und HerrickPayoffIndex
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'HerrickPayoffIndex': {
                'class': HerrickPayoffIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HerrickPayoffIndex'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'HerrickPayoffIndex': 1.0
        })
    )
