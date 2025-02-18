import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_MarketDepthHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und MarketDepthHeatmap
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'MarketDepthHeatmap': {
                'class': MarketDepthHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketDepthHeatmap'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'MarketDepthHeatmap': 1.0
        })
    )
