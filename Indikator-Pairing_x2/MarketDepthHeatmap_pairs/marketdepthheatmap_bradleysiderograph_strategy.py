import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'BradleySiderograph': 1.0
        })
    )
