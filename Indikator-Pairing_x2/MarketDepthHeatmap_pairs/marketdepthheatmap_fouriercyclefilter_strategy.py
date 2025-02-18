import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
