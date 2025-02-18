import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_VolumeRateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und VolumeRateOfChange
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'VolumeRateOfChange': {
                'class': VolumeRateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeRateOfChange'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'VolumeRateOfChange': 1.0
        })
    )
