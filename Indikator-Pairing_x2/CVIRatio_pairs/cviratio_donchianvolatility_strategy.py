import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CVIRatio_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CVIRatio und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'CVIRatio': {
                'class': CVIRatio,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CVIRatio'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'CVIRatio': 1.0,
            'DonchianVolatility': 1.0
        })
    )
