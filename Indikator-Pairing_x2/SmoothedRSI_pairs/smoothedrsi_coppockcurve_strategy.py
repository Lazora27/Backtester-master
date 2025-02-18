import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'CoppockCurve': 1.0
        })
    )
