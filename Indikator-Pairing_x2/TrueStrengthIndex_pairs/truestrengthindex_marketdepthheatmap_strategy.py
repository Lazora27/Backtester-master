import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
