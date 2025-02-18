import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
