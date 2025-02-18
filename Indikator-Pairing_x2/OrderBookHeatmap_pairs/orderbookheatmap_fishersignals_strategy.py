import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OrderBookHeatmap_FisherSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OrderBookHeatmap und FisherSignals
    """
    
    params = (
        ('indicators', {
            'OrderBookHeatmap': {
                'class': OrderBookHeatmap,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OrderBookHeatmap'>
            },
            'FisherSignals': {
                'class': FisherSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherSignals'>
            }
        }),
        ('weights', {
            'OrderBookHeatmap': 1.0,
            'FisherSignals': 1.0
        })
    )
