import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'CoppockCurve': 1.0
        })
    )
