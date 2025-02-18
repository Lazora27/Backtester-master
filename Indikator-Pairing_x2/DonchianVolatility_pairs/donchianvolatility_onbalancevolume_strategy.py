import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_OnBalanceVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und OnBalanceVolume
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'OnBalanceVolume': {
                'class': OnBalanceVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_OnBalanceVolume'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'OnBalanceVolume': 1.0
        })
    )
