import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_WolfeWaves_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und WolfeWaves
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'WolfeWaves': 1.0
        })
    )
