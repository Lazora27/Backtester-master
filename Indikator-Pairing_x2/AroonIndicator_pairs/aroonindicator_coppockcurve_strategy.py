import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AroonIndicator_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AroonIndicator und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'AroonIndicator': {
                'class': AroonIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AroonIndicator'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'AroonIndicator': 1.0,
            'CoppockCurve': 1.0
        })
    )
