import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_AccumulationDistributionLine_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und AccumulationDistributionLine
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'AccumulationDistributionLine': {
                'class': AccumulationDistributionLine,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccumulationDistributionLine'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'AccumulationDistributionLine': 1.0
        })
    )
