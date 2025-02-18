import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und BarStrength
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'BarStrength': 1.0
        })
    )
