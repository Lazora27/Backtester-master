import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DynamicMomentumIndex_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DynamicMomentumIndex und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'DynamicMomentumIndex': {
                'class': DynamicMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DynamicMomentumIndex'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'DynamicMomentumIndex': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
