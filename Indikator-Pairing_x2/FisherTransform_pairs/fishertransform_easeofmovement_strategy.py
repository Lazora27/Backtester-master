import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_EaseOfMovement_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und EaseOfMovement
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'EaseOfMovement': {
                'class': EaseOfMovement,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EaseOfMovement1'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'EaseOfMovement': 1.0
        })
    )
