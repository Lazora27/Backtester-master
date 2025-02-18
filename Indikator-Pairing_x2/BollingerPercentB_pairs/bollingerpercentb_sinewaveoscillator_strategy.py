import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerPercentB_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerPercentB und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'BollingerPercentB': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
