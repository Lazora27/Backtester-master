import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TrueRange_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TrueRange und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'TrueRange': {
                'class': TrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrueRange1'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'TrueRange': 1.0,
            'DonchianVolatility': 1.0
        })
    )
