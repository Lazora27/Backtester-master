import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'PhaseDivergence': 1.0
        })
    )
