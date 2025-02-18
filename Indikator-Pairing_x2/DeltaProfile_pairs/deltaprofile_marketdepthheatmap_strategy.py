import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DeltaProfile_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DeltaProfile und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'DeltaProfile': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
