import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedATR_SineWaveAdaptive_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedATR und SineWaveAdaptive
    """
    
    params = (
        ('indicators', {
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            },
            'SineWaveAdaptive': {
                'class': SineWaveAdaptive,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SineWaveAdaptive'>
            }
        }),
        ('weights', {
            'ModifiedATR': 1.0,
            'SineWaveAdaptive': 1.0
        })
    )
