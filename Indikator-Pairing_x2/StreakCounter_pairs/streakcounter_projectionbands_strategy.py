import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_ProjectionBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und ProjectionBands
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'ProjectionBands': {
                'class': ProjectionBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionBands'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'ProjectionBands': 1.0
        })
    )
