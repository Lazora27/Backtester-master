import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdvanceDeclineLine_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdvanceDeclineLine und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'AdvanceDeclineLine': {
                'class': AdvanceDeclineLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdvanceDeclineLine'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'AdvanceDeclineLine': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
