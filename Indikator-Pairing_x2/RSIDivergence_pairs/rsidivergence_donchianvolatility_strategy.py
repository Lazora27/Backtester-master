import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RSIDivergence_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RSIDivergence und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'RSIDivergence': {
                'class': RSIDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RSIDivergence'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'RSIDivergence': 1.0,
            'DonchianVolatility': 1.0
        })
    )
