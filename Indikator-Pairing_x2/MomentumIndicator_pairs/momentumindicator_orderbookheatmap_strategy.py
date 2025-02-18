import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumIndicator_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumIndicator und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'MomentumIndicator': {
                'class': MomentumIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumIndicator'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'MomentumIndicator': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
