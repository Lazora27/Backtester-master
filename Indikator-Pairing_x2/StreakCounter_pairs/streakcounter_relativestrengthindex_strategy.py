import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_RelativeStrengthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und RelativeStrengthIndex
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'RelativeStrengthIndex': 1.0
        })
    )
