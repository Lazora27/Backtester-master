import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDHistogram_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDHistogram und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'MACDHistogram': {
                'class': MACDHistogram,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDHistogram'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'MACDHistogram': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
