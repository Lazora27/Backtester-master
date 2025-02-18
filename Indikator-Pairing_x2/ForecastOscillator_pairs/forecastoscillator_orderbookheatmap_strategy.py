import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
