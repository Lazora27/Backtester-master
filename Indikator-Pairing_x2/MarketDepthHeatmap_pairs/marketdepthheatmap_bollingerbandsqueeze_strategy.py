import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
