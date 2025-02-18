import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'ModifiedATR': 1.0
        })
    )
