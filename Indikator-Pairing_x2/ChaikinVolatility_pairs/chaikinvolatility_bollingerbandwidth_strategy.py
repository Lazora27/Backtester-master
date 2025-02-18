import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChaikinVolatility_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChaikinVolatility und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'ChaikinVolatility': {
                'class': ChaikinVolatility,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinVolatility'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'ChaikinVolatility': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
