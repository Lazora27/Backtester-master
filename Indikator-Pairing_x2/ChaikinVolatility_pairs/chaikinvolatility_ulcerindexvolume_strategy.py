import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
