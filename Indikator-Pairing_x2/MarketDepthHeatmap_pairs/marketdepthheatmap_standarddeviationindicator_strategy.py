import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_StandardDeviationIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und StandardDeviationIndicator
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'StandardDeviationIndicator': {
                'class': StandardDeviationIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StandardDeviationIndicator'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'StandardDeviationIndicator': 1.0
        })
    )
