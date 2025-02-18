import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'DonchianVolatility': 1.0
        })
    )
