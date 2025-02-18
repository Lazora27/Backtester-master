import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
