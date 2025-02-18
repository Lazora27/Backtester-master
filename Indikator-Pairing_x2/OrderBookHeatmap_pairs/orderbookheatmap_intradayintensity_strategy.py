import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_IntradayIntensity_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und IntradayIntensity
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'IntradayIntensity': {
                'class': IntradayIntensity,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IntradayIntensity'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'IntradayIntensity': 1.0
        })
    )
