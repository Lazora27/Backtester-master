import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und BarStrength
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'BarStrength': 1.0
        })
    )
