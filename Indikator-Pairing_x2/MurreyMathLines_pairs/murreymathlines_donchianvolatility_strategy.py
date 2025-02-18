import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MurreyMathLines_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MurreyMathLines und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'MurreyMathLines': {
                'class': MurreyMathLines,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MurreyMathLines'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'MurreyMathLines': 1.0,
            'DonchianVolatility': 1.0
        })
    )
