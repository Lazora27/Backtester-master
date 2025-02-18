import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceRateOfChange_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceRateOfChange und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'PriceRateOfChange': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
