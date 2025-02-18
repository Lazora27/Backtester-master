import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'BradleySiderograph': 1.0
        })
    )
