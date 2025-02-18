import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'BollingerPercentB': 1.0
        })
    )
