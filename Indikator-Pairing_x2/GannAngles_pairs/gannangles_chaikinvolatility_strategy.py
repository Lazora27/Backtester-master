import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannAngles_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannAngles und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'GannAngles': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
