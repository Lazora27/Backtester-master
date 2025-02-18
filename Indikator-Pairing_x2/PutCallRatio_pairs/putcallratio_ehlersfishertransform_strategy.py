import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PutCallRatio_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PutCallRatio und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'PutCallRatio': {
                'class': PutCallRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PutCallRatio1'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'PutCallRatio': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
