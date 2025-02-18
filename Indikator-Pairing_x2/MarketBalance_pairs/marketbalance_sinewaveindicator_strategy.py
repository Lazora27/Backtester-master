import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
