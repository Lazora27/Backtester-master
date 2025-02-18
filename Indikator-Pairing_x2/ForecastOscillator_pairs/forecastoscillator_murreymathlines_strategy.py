import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ForecastOscillator_MurreyMathLines_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ForecastOscillator und MurreyMathLines
    """
    
    params = (
        ('indicators', {
            'ForecastOscillator': {
                'class': ForecastOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ForecastOscillator'>
            },
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            }
        }),
        ('weights', {
            'ForecastOscillator': 1.0,
            'MurreyMathLines': 1.0
        })
    )
