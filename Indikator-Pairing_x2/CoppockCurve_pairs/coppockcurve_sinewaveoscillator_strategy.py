import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
