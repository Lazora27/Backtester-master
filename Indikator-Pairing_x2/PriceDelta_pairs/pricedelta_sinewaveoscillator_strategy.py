import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
