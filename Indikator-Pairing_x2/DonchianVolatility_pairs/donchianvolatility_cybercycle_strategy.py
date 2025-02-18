import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_CyberCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und CyberCycle
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'CyberCycle': {
                'class': CyberCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CyberCycle'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'CyberCycle': 1.0
        })
    )
