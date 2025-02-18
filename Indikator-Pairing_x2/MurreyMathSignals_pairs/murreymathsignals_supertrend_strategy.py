import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_SuperTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und SuperTrend
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'SuperTrend': {
                'class': SuperTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperTrend'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'SuperTrend': 1.0
        })
    )
