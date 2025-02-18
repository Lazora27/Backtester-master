import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_StreakCounter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und StreakCounter
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'StreakCounter': 1.0
        })
    )
