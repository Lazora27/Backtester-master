import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketDepthHeatmap_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketDepthHeatmap und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'MarketDepthHeatmap': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
