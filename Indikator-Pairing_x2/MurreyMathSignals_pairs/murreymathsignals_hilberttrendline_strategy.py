import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_HilbertTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und HilbertTrendline
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'HilbertTrendline': {
                'class': HilbertTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendline'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'HilbertTrendline': 1.0
        })
    )
