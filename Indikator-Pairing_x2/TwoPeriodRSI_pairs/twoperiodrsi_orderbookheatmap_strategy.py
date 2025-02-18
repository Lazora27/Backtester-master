import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TwoPeriodRSI_OrderBookHeatmap_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TwoPeriodRSI und OrderBookHeatmap
    """
    
    params = (
        ('indicators', {
            'TwoPeriodRSI': {
                'class': TwoPeriodRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TwoPeriodRSI'>
            },
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            }
        }),
        ('weights', {
            'TwoPeriodRSI': 1.0,
            'OrderBookHeatmap': 1.0
        })
    )
