import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
