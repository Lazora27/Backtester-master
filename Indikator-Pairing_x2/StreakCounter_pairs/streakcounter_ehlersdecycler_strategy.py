import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'EhlersDecycler': 1.0
        })
    )
