import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueStrengthIndex_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueStrengthIndex und MarketBalance
    """
    
    params = (
        ('indicators', {
            'TrueStrengthIndex': {
                'class': TrueStrengthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueStrengthIndex'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'TrueStrengthIndex': 1.0,
            'MarketBalance': 1.0
        })
    )
