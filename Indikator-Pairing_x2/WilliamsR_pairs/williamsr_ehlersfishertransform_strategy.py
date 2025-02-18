import backtrader as bt
from ..base_strategy import FlexibleStrategy

class WilliamsR_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von WilliamsR und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'WilliamsR': {
                'class': WilliamsR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WilliamsR1'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'WilliamsR': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
