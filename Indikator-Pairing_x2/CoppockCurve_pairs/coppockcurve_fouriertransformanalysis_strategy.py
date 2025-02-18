import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_FourierTransformAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und FourierTransformAnalysis
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'FourierTransformAnalysis': {
                'class': FourierTransformAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierTransformAnalysis'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'FourierTransformAnalysis': 1.0
        })
    )
