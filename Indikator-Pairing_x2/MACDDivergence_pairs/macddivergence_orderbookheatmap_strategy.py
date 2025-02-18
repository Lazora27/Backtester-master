import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
