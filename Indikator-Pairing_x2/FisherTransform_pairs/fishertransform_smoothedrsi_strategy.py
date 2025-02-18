import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'SmoothedRSI': 1.0
        })
    )
