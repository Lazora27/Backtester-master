import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und MarketBalance
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'MarketBalance': 1.0
        })
    )
