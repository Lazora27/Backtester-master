import backtrader as bt
from ..base_strategy import FlexibleStrategy

class FisherTransform_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von FisherTransform und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'FisherTransform': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
