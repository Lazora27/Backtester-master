import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_RelativeVigorIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und RelativeVigorIndex
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'RelativeVigorIndex': {
                'class': RelativeVigorIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeVigorIndex'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'RelativeVigorIndex': 1.0
        })
    )
