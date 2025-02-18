import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersFisherTransform_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersFisherTransform und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'EhlersFisherTransform': {
                'class': EhlersFisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersFisherTransform'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'EhlersFisherTransform': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
