import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und TrendCycles
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'TrendCycles': 1.0
        })
    )
