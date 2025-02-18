import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeKrollStop_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeKrollStop und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'ChandeKrollStop': {
                'class': ChandeKrollStop,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeKrollStop'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'ChandeKrollStop': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
