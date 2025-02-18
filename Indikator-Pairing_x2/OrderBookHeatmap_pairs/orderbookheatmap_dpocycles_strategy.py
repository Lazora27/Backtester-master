import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_DPOCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und DPOCycles
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'DPOCycles': {
                'class': DPOCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DPOCycles'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'DPOCycles': 1.0
        })
    )
