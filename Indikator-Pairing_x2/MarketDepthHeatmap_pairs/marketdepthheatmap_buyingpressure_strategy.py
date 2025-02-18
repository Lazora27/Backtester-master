import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_BuyingPressure_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und BuyingPressure
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'BuyingPressure': {
                'class': BuyingPressure,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BuyingPressure'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'BuyingPressure': 1.0
        })
    )
