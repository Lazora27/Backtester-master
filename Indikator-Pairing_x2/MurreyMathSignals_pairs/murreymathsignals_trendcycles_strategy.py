import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und TrendCycles
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'TrendCycles': 1.0
        })
    )
