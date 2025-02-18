import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_MarketFacilitationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und MarketFacilitationIndex
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'MarketFacilitationIndex': {
                'class': MarketFacilitationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketFacilitationIndex'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'MarketFacilitationIndex': 1.0
        })
    )
