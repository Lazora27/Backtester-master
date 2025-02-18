import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'CoppockCurve': 1.0
        })
    )
