import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_DonchianChannels_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und DonchianChannels
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'DonchianChannels': {
                'class': DonchianChannels,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianChannels'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'DonchianChannels': 1.0
        })
    )
