import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
