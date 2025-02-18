import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_FlowOfFunds_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und FlowOfFunds
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'FlowOfFunds': {
                'class': FlowOfFunds,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FlowOfFunds'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'FlowOfFunds': 1.0
        })
    )
