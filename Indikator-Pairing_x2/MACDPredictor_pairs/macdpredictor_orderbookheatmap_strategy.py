import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDPredictor_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDPredictor und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'MACDPredictor': {
                'class': MACDPredictor,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDPredictor'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'MACDPredictor': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
