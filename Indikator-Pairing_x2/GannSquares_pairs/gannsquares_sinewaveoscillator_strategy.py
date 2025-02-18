import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
