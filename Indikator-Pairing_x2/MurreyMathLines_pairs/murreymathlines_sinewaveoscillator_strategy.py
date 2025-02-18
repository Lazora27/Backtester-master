import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
