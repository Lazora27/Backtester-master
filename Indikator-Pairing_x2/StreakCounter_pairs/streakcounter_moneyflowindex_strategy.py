import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_MoneyFlowIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und MoneyFlowIndex
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'MoneyFlowIndex': {
                'class': MoneyFlowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MoneyFlowIndex'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'MoneyFlowIndex': 1.0
        })
    )
