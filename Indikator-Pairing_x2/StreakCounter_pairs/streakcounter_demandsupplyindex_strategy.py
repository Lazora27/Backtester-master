import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_DemandSupplyIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und DemandSupplyIndex
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'DemandSupplyIndex': {
                'class': DemandSupplyIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandSupplyIndex'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'DemandSupplyIndex': 1.0
        })
    )
