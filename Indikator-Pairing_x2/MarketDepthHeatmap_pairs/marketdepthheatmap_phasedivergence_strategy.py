import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'PhaseDivergence': 1.0
        })
    )
