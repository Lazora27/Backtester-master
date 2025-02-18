import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_StreakCounter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und StreakCounter
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'StreakCounter': 1.0
        })
    )
