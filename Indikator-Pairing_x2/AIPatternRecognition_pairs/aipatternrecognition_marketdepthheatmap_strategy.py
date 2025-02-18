import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AIPatternRecognition_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AIPatternRecognition und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'AIPatternRecognition': {
                'class': AIPatternRecognition,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AIPatternRecognition'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'AIPatternRecognition': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
