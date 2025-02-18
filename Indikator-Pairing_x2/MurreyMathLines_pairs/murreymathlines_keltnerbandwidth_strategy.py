import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
