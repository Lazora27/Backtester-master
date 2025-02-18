import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_VWAPDeviationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und VWAPDeviationBands
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'VWAPDeviationBands': {
                'class': VWAPDeviationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPDeviationBands'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'VWAPDeviationBands': 1.0
        })
    )
