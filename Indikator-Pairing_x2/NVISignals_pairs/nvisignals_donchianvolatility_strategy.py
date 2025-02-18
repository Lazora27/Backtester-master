import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NVISignals_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NVISignals und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'NVISignals': {
                'class': NVISignals,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NVISignals'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'NVISignals': 1.0,
            'DonchianVolatility': 1.0
        })
    )
