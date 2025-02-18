import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
