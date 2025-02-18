import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MarketBalance_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MarketBalance und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'MarketBalance': {
                'class': MarketBalance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MarketBalance'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'MarketBalance': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
