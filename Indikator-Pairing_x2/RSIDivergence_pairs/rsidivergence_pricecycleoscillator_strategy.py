import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
