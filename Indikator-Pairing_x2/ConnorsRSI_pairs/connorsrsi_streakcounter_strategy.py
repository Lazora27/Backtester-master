import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ConnorsRSI_StreakCounter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ConnorsRSI und StreakCounter
    """
    
    params = (
        ('indicators', {
            'ConnorsRSI': {
                'class': ConnorsRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ConnorsRSI'>
            },
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            }
        }),
        ('weights', {
            'ConnorsRSI': 1.0,
            'StreakCounter': 1.0
        })
    )
