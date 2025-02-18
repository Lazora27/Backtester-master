import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_CyberCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und CyberCycleOscillator
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'CyberCycleOscillator': {
                'class': CyberCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycleOscillator'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'CyberCycleOscillator': 1.0
        })
    )
