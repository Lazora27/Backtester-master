import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_DecyclerOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und DecyclerOscillator
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'DecyclerOscillator': {
                'class': DecyclerOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DecyclerOscillator'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'DecyclerOscillator': 1.0
        })
    )
