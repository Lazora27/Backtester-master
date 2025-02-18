import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AwesomeOscillator_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AwesomeOscillator und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'AwesomeOscillator': {
                'class': AwesomeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AwesomeOscillator1'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'AwesomeOscillator': 1.0,
            'ModifiedATR': 1.0
        })
    )
