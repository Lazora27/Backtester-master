import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanOscillator_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanOscillator und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'McClellanOscillator': {
                'class': McClellanOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanOscillator'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'McClellanOscillator': 1.0,
            'CoppockCurve': 1.0
        })
    )
