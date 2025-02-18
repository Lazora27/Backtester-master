import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersFisherTransform_WeeklyCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersFisherTransform und WeeklyCycle
    """
    
    params = (
        ('indicators', {
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            },
            'WeeklyCycle': {
                'class': WeeklyCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeeklyCycle'>
            }
        }),
        ('weights', {
            'EhlersFisherTransform': 1.0,
            'WeeklyCycle': 1.0
        })
    )
