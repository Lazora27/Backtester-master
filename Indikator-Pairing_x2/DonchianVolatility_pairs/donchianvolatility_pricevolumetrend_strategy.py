import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_PriceVolumeTrend_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und PriceVolumeTrend
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'PriceVolumeTrend': {
                'class': PriceVolumeTrend,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PriceVolumeTrend'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'PriceVolumeTrend': 1.0
        })
    )
