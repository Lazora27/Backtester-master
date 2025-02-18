import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RelativeStrengthIndex_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RelativeStrengthIndex und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'RelativeStrengthIndex': {
                'class': RelativeStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RelativeStrengthIndex1'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'RelativeStrengthIndex': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
