import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_SymmetricalTriangle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und SymmetricalTriangle
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'SymmetricalTriangle': {
                'class': SymmetricalTriangle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SymmetricalTriangle'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'SymmetricalTriangle': 1.0
        })
    )
