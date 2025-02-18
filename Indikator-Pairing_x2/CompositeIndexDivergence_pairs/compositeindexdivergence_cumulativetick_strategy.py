import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_CumulativeTick_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und CumulativeTick
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'CumulativeTick': 1.0
        })
    )
