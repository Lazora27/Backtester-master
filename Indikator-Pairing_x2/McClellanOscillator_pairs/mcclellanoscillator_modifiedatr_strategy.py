import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'ModifiedATR': 1.0
        })
    )
