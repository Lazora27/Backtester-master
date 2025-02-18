import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und CCITurbo
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'CCITurbo': 1.0
        })
    )
