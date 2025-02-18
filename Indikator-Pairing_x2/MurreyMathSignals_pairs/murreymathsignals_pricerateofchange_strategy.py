import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_PriceRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und PriceRateOfChange
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'PriceRateOfChange': {
                'class': PriceRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceRateOfChange'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'PriceRateOfChange': 1.0
        })
    )
