import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'ProjectionBands': 1.0
        })
    )
