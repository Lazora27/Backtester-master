import backtrader as bt
from ..base_strategy import FlexibleStrategy

class Fisher_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von Fisher und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'Fisher': {
                'class': Fisher,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_Fisher'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'Fisher': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
