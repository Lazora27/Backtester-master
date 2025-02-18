import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
