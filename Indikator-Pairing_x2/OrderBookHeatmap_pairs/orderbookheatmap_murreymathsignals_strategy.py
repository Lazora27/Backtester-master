import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
