import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveATR_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveATR und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'AdaptiveATR': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
