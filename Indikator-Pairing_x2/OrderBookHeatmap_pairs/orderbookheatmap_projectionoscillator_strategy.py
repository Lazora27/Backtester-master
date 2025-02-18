import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_ProjectionOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und ProjectionOscillator
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'ProjectionOscillator': {
                'class': ProjectionOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ProjectionOscillator'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'ProjectionOscillator': 1.0
        })
    )
