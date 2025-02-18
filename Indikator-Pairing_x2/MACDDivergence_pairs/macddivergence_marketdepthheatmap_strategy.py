import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
