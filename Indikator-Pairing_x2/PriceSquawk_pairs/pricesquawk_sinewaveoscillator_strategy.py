import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceSquawk_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceSquawk und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'PriceSquawk': {
                'class': PriceSquawk,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceSquawk'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'PriceSquawk': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
