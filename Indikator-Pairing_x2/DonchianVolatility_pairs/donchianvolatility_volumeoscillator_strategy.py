import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_VolumeOscillator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und VolumeOscillator
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'VolumeOscillator': {
                'class': VolumeOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeOscillator'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'VolumeOscillator': 1.0
        })
    )
