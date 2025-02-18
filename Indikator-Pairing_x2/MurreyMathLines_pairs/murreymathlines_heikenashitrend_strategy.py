import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_HeikenAshiTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und HeikenAshiTrend
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'HeikenAshiTrend': {
                'class': HeikenAshiTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HeikenAshiTrend'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'HeikenAshiTrend': 1.0
        })
    )
