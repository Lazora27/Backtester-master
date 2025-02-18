import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HullMovingAverage_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HullMovingAverage und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'HullMovingAverage': {
                'class': HullMovingAverage,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HullMovingAverage'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'HullMovingAverage': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
