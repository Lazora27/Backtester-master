import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MACDDivergence_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MACDDivergence und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'MACDDivergence': {
                'class': MACDDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MACDDivergence'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'MACDDivergence': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
