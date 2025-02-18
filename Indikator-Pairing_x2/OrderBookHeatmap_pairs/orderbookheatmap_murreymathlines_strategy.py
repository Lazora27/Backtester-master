import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'MurreyMathLines': 1.0
        })
    )
