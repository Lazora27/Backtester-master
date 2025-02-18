import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'AverageLogRange': 1.0
        })
    )
