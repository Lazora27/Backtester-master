import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'CoppockCurve': 1.0
        })
    )
