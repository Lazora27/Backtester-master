import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WolfeWaveIndicator_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WolfeWaveIndicator und MarketBalance
    """
    
    params = (
        ('indicators', {
            'WolfeWaveIndicator': {
                'class': WolfeWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WolfeWaveIndicator'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'WolfeWaveIndicator': 1.0,
            'MarketBalance': 1.0
        })
    )
