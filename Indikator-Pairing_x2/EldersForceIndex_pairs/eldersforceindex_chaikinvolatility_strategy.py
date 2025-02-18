import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
