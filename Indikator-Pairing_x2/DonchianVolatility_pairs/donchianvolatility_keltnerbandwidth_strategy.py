import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
