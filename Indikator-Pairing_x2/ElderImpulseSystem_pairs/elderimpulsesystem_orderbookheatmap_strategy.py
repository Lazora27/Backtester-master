import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
