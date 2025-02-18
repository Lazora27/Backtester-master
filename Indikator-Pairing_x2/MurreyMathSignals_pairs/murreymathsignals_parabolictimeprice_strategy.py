import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
