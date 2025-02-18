import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und MarketBalance
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'MarketBalance': 1.0
        })
    )
