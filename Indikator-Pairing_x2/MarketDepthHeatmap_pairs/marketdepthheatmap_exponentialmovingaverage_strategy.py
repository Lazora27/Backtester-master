import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_ExponentialMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und ExponentialMovingAverage
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'ExponentialMovingAverage': {
                'class': ExponentialMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ExponentialMovingAverage'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'ExponentialMovingAverage': 1.0
        })
    )
