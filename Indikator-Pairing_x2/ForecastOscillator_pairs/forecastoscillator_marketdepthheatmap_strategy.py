import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
