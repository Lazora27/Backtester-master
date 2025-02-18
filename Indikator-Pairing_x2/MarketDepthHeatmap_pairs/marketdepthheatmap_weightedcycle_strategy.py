import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'WeightedCycle': 1.0
        })
    )
