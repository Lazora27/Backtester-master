import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WyckoffWaveIndicator_MarketBalance_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WyckoffWaveIndicator und MarketBalance
    """
    
    params = (
        ('indicators', {
            'WyckoffWaveIndicator': {
                'class': WyckoffWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WyckoffWaveIndicator'>
            },
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            }
        }),
        ('weights', {
            'WyckoffWaveIndicator': 1.0,
            'MarketBalance': 1.0
        })
    )
