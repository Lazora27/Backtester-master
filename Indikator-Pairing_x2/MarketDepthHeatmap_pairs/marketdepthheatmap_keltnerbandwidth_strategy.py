import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
