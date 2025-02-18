import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'CoppockCurve': 1.0
        })
    )
