import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
