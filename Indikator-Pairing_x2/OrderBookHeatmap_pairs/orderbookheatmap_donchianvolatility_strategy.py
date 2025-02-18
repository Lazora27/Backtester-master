import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'DonchianVolatility': 1.0
        })
    )
