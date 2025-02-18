import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_RoundNumbersIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und RoundNumbersIndicator
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'RoundNumbersIndicator': {
                'class': RoundNumbersIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RoundNumbersIndicator'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'RoundNumbersIndicator': 1.0
        })
    )
