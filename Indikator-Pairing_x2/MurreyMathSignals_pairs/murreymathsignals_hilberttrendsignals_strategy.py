import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
