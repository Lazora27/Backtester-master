import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AdaptiveRSI_FisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AdaptiveRSI und FisherTransform
    """
    
    params = (
        ('indicators', {
            'AdaptiveRSI': {
                'class': AdaptiveRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveRSI'>
            },
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            }
        }),
        ('weights', {
            'AdaptiveRSI': 1.0,
            'FisherTransform': 1.0
        })
    )
