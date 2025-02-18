import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_TrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und TrueRange
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'TrueRange': 1.0
        })
    )
