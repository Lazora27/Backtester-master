import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_SuperMACD_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und SuperMACD
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'SuperMACD': 1.0
        })
    )
