import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_PriceCycleOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und PriceCycleOscillator
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'PriceCycleOscillator': {
                'class': PriceCycleOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceCycleOscillator'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'PriceCycleOscillator': 1.0
        })
    )
