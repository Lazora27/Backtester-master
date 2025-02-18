import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PercentagePriceOscillator_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PercentagePriceOscillator und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'PercentagePriceOscillator': {
                'class': PercentagePriceOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PercentagePriceOscillator'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'PercentagePriceOscillator': 1.0,
            'MurreyMathLines': 1.0
        })
    )
