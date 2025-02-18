import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_MarketOrderFlow_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und MarketOrderFlow
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'MarketOrderFlow': {
                'class': MarketOrderFlow,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketOrderFlow'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'MarketOrderFlow': 1.0
        })
    )
