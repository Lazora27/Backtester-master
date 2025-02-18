import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
