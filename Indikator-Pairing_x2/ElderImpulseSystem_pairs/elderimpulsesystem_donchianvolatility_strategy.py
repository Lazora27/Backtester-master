import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_DonchianVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und DonchianVolatility
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'DonchianVolatility': {
                'class': DonchianVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DonchianVolatility'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'DonchianVolatility': 1.0
        })
    )
