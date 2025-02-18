import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DOMDepth_MurreyMathSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DOMDepth und MurreyMathSignals
    """
    
    params = (
        ('indicators', {
            'DOMDepth': {
                'class': DOMDepth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DOMDepth'>
            },
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            }
        }),
        ('weights', {
            'DOMDepth': 1.0,
            'MurreyMathSignals': 1.0
        })
    )
