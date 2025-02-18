import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'CoppockCurve': 1.0
        })
    )
