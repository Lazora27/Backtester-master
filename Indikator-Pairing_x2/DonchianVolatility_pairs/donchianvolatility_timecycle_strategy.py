import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und TimeCycle
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'TimeCycle': 1.0
        })
    )
