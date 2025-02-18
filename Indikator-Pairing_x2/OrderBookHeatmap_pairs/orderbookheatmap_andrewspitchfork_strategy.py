import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_AndrewsPitchfork_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und AndrewsPitchfork
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'AndrewsPitchfork': {
                'class': AndrewsPitchfork,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AndrewsPitchfork'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'AndrewsPitchfork': 1.0
        })
    )
