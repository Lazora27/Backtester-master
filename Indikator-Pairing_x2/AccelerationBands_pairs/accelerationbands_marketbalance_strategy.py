import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AccelerationBands_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AccelerationBands und MarketBalance
    """
    
    params = (
        ('indicators', {
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'AccelerationBands': 1.0,
            'MarketBalance': 1.0
        })
    )
