import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
