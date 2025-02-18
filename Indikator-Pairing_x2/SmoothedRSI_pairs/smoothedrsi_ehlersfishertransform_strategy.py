import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SmoothedRSI_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SmoothedRSI und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'SmoothedRSI': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
