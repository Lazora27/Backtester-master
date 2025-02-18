import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
