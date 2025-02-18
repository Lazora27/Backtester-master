import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_ModifiedATR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und ModifiedATR
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'ModifiedATR': {
                'class': ModifiedATR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedATR'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'ModifiedATR': 1.0
        })
    )
