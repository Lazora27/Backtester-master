import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'WolfeWaves': 1.0
        })
    )
