import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_WeightedMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und WeightedMovingAverage
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'WeightedMovingAverage': {
                'class': WeightedMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedMovingAverage'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'WeightedMovingAverage': 1.0
        })
    )
