import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'WeightedCycle': 1.0
        })
    )
