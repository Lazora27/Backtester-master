import backtrader as bt
from ..base_strategy import FlexibleStrategy

class DonchianVolatility_PhaseDivergence_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von DonchianVolatility und PhaseDivergence
    """
    
    params = (
        ('indicators', {
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            },
            'PhaseDivergence': {
                'class': PhaseDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PhaseDivergence'>
            }
        }),
        ('weights', {
            'DonchianVolatility': 1.0,
            'PhaseDivergence': 1.0
        })
    )
