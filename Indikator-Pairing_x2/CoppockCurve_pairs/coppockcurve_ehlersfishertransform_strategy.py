import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
