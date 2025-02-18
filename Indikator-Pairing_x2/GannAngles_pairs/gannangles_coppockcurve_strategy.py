import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'CoppockCurve': 1.0
        })
    )
