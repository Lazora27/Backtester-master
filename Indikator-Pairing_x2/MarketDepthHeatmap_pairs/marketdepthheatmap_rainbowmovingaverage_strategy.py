import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_RainbowMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und RainbowMovingAverage
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'RainbowMovingAverage': {
                'class': RainbowMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RainbowMovingAverage'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'RainbowMovingAverage': 1.0
        })
    )
