import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
