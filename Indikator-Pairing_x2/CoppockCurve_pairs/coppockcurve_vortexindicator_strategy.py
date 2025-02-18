import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'VortexIndicator': 1.0
        })
    )
