import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'EhlersDecycler': 1.0
        })
    )
