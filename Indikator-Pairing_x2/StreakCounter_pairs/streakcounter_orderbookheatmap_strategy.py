import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StreakCounter_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StreakCounter und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'StreakCounter': {
                'class': StreakCounter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StreakCounter'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'StreakCounter': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
