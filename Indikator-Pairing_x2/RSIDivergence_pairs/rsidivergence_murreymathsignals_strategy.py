import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
