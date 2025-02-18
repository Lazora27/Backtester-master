import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und CCITurbo
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'CCITurbo': 1.0
        })
    )
