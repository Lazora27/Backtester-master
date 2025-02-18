import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
