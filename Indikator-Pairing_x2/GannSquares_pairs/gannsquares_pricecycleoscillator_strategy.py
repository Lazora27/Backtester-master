import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannSquares_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannSquares und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'GannSquares': {
                'class': GannSquares,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannSquares'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'GannSquares': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
