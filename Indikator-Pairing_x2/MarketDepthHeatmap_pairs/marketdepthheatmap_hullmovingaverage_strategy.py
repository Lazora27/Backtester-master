import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_HullMovingAverage_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und HullMovingAverage
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'HullMovingAverage': 1.0
        })
    )
