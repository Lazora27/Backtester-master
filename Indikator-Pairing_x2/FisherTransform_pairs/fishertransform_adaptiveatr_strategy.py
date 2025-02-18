import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_AdaptiveATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und AdaptiveATR
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'AdaptiveATR': {
                'class': AdaptiveATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AdaptiveATR'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'AdaptiveATR': 1.0
        })
    )
