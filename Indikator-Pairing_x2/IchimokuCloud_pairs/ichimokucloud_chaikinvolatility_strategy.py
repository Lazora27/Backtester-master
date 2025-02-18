import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
