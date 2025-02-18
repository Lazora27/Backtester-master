import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PriceDelta_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PriceDelta und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'PriceDelta': {
                'class': PriceDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceDelta'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'PriceDelta': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
