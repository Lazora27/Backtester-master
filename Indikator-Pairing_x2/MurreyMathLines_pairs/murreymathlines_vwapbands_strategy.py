import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_VWAPBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und VWAPBands
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'VWAPBands': 1.0
        })
    )
