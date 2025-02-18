import backtrader as bt
from ..base_strategy import FlexibleStrategy

class UltimateOscillator_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von UltimateOscillator und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'UltimateOscillator': {
                'class': UltimateOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UltimateOscillator1'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'UltimateOscillator': 1.0,
            'CoppockCurve': 1.0
        })
    )
