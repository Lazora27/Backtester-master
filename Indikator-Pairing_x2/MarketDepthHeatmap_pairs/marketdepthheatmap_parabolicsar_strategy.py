import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'ParabolicSAR': 1.0
        })
    )
