import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_SeasonalStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und SeasonalStrength
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'SeasonalStrength': {
                'class': SeasonalStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SeasonalStrength'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'SeasonalStrength': 1.0
        })
    )
