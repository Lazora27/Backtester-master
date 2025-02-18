import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
