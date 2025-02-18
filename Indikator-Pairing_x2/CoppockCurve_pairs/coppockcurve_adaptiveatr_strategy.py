import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'AdaptiveATR': 1.0
        })
    )
