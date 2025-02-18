import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_HilbertTrendSignals_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und HilbertTrendSignals
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'HilbertTrendSignals': {
                'class': HilbertTrendSignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertTrendSignals'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'HilbertTrendSignals': 1.0
        })
    )
