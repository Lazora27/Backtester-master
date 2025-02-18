import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_SineWaveOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und SineWaveOscillator
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'SineWaveOscillator': {
                'class': SineWaveOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveOscillator'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'SineWaveOscillator': 1.0
        })
    )
