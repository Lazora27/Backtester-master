import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EaseOfMovement_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EaseOfMovement und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'EaseOfMovement': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
