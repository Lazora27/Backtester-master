import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CompositeIndexDivergence_StreakCounter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CompositeIndexDivergence und StreakCounter
    """
    
    params = (
        ('indicators', {
            'CompositeIndexDivergence': {
                'class': CompositeIndexDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CompositeIndexDivergence'>
            },
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            }
        }),
        ('weights', {
            'CompositeIndexDivergence': 1.0,
            'StreakCounter': 1.0
        })
    )
