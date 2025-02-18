import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TimeSalesVolume_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TimeSalesVolume und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'TimeSalesVolume': {
                'class': TimeSalesVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeSalesVolume'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'TimeSalesVolume': 1.0,
            'DonchianVolatility': 1.0
        })
    )
