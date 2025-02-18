import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BalanceMomentum_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BalanceMomentum und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'BalanceMomentum': {
                'class': BalanceMomentum,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BalanceMomentum'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'BalanceMomentum': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
