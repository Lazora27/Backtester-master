import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
