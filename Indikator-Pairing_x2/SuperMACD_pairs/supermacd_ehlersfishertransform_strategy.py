import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_EhlersFisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und EhlersFisherTransform
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'EhlersFisherTransform': 1.0
        })
    )
