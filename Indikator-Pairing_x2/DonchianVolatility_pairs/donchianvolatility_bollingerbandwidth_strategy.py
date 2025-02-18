import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
