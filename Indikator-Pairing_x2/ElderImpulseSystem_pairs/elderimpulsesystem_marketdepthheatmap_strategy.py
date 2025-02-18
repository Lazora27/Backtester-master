import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
