import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_HilbertDominantCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und HilbertDominantCycle
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'HilbertDominantCycle': {
                'class': HilbertDominantCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HilbertDominantCycle'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'HilbertDominantCycle': 1.0
        })
    )
