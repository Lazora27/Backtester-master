import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
