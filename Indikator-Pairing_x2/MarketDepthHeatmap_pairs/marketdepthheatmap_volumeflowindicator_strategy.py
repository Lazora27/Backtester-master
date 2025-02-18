import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_VolumeFlowIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und VolumeFlowIndicator
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'VolumeFlowIndicator': 1.0
        })
    )
