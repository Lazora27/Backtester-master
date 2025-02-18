import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'DonchianVolatility': 1.0
        })
    )
