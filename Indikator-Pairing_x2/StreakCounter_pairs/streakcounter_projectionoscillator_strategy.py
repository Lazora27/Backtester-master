import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
