import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathSignals_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathSignals und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'MurreyMathSignals': {
                'class': MurreyMathSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathSignals'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'MurreyMathSignals': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
