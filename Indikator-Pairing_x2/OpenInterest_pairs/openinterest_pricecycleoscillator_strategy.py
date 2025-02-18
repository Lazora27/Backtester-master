import backtrader as bt
from ..base_strategy import FlexibleStrategy

class OpenInterest_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von OpenInterest und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'OpenInterest': {
                'class': OpenInterest,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OpenInterest'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'OpenInterest': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
