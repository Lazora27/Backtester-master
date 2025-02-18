import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_ChaikinVolatility_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und ChaikinVolatility
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'ChaikinVolatility': 1.0
        })
    )
