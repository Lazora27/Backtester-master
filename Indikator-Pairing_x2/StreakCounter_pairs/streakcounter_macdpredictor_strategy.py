import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_MACDPredictor_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und MACDPredictor
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'MACDPredictor': 1.0
        })
    )
