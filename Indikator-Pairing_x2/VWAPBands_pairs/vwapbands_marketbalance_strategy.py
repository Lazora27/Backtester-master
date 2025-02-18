import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und MarketBalance
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'MarketBalance': 1.0
        })
    )
