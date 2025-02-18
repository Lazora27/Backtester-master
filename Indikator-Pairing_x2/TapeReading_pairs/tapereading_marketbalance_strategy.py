import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und MarketBalance
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'MarketBalance': 1.0
        })
    )
