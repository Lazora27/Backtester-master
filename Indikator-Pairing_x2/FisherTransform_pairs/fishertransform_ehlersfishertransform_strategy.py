import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
