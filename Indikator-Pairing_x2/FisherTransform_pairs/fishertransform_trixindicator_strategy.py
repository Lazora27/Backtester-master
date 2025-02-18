import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_TRIXIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und TRIXIndicator
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'TRIXIndicator': {
                'class': TRIXIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TRIXIndicator'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'TRIXIndicator': 1.0
        })
    )
