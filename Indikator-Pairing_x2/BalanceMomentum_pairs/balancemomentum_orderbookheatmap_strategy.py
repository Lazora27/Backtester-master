import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
