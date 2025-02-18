import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PivotPoints_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PivotPoints und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'PivotPoints': {
                'class': PivotPoints,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PivotPoints'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'PivotPoints': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
