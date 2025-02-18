import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und MarketBalance
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'MarketBalance': 1.0
        })
    )
