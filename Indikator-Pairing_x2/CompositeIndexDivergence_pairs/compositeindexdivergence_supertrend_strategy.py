import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und SuperTrend
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'SuperTrend': 1.0
        })
    )
