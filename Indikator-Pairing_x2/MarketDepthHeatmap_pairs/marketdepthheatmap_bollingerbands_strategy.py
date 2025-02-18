import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und BollingerBands
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'BollingerBands': 1.0
        })
    )
