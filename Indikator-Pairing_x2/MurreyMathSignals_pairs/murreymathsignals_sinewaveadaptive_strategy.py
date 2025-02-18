import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
