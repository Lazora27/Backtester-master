import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
