import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickVolume_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickVolume und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'TickVolume': {
                'class': TickVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickVolume'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'TickVolume': 1.0,
            'DonchianVolatility': 1.0
        })
    )
