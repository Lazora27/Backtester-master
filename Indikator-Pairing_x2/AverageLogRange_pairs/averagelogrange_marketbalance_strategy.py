import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und MarketBalance
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'MarketBalance': 1.0
        })
    )
