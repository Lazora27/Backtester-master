import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinOscillator_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinOscillator und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'ChaikinOscillator': {
                'class': ChaikinOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinOscillator'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'ChaikinOscillator': 1.0,
            'CoppockCurve': 1.0
        })
    )
