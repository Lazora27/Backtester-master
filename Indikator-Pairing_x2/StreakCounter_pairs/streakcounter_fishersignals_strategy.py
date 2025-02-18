import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und FisherSignals
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'FisherSignals': 1.0
        })
    )
