import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'DonchianVolatility': 1.0
        })
    )
