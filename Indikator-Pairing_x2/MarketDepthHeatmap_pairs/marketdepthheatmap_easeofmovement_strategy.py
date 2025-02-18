import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'EaseOfMovement': 1.0
        })
    )
