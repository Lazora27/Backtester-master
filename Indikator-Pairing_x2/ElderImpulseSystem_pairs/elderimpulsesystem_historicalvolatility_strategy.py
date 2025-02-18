import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ElderImpulseSystem_HistoricalVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ElderImpulseSystem und HistoricalVolatility
    """
    
    params = (
        ('indicators', {
            'ElderImpulseSystem': {
                'class': ElderImpulseSystem,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ElderImpulseSystem'>
            },
            'HistoricalVolatility': {
                'class': HistoricalVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HistoricalVolatility'>
            }
        }),
        ('weights', {
            'ElderImpulseSystem': 1.0,
            'HistoricalVolatility': 1.0
        })
    )
