import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
