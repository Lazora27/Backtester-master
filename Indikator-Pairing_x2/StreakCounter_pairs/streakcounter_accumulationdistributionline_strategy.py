import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
