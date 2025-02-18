import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CoppockCurve_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CoppockCurve und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'CoppockCurve': {
                'class': CoppockCurve,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CoppockCurve'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'CoppockCurve': 1.0,
            'DonchianVolatility': 1.0
        })
    )
