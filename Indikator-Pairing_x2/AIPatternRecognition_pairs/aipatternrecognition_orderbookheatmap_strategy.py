import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
