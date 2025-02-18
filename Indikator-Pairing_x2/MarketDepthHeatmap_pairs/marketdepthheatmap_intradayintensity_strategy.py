import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'IntradayIntensity': 1.0
        })
    )
