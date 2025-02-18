import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TapeReading_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TapeReading und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'TapeReading': {
                'class': TapeReading,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TapeReading'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'TapeReading': 1.0,
            'DonchianVolatility': 1.0
        })
    )
