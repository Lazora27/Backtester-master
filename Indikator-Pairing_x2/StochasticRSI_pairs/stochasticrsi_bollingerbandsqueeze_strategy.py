import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
