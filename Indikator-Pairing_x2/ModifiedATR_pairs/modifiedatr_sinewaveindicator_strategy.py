import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_SineWaveIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und SineWaveIndicator
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'SineWaveIndicator': {
                'class': SineWaveIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveIndicator'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'SineWaveIndicator': 1.0
        })
    )
