import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_AccelerationBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und AccelerationBands
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'AccelerationBands': {
                'class': AccelerationBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AccelerationBands'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'AccelerationBands': 1.0
        })
    )
