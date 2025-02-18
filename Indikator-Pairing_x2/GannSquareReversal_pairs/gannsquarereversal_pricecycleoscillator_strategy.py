import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquareReversal_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquareReversal und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'GannSquareReversal': {
                'class': GannSquareReversal,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquareReversal'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'GannSquareReversal': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
