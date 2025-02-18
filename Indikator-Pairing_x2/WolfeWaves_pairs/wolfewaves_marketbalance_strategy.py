import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaves_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaves und MarketBalance
    """
    
    params = (
        ('indicators', {
            'WolfeWaves': {
                'class': WolfeWaves,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaves'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'WolfeWaves': 1.0,
            'MarketBalance': 1.0
        })
    )
