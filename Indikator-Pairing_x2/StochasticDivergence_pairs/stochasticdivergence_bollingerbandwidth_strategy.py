import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
