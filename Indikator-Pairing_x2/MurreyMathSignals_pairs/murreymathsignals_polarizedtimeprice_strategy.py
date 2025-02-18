import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_PolarizedTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und PolarizedTimePrice
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'PolarizedTimePrice': {
                'class': PolarizedTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PolarizedTimePrice'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'PolarizedTimePrice': 1.0
        })
    )
