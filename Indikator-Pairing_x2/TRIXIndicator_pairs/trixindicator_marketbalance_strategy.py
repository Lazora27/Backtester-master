import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TRIXIndicator_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TRIXIndicator und MarketBalance
    """
    
    params = (
        ('indicators', {
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'TRIXIndicator': 1.0,
            'MarketBalance': 1.0
        })
    )
