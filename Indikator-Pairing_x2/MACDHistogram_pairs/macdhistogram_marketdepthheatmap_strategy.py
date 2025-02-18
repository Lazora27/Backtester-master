import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
