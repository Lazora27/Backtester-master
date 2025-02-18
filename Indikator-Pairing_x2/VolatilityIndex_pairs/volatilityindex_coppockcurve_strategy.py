import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolatilityIndex_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolatilityIndex und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'VolatilityIndex': {
                'class': VolatilityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolatilityIndex'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'VolatilityIndex': 1.0,
            'CoppockCurve': 1.0
        })
    )
