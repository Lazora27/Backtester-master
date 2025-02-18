import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_CoppockCurve_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und CoppockCurve
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'CoppockCurve': 1.0
        })
    )
