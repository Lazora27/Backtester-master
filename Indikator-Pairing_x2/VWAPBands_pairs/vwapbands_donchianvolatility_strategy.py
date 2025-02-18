import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPBands_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPBands und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'VWAPBands': {
                'class': VWAPBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPBands'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'VWAPBands': 1.0,
            'DonchianVolatility': 1.0
        })
    )
