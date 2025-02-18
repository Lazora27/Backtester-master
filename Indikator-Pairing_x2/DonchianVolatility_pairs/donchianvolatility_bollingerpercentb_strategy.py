import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'BollingerPercentB': 1.0
        })
    )
