import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
