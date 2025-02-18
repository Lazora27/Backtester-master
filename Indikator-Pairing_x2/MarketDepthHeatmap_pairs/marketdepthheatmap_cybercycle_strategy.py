import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und CyberCycle
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'CyberCycle': 1.0
        })
    )
