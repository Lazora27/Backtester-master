import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_BollingerBandSqueeze_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und BollingerBandSqueeze
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'BollingerBandSqueeze': {
                'class': BollingerBandSqueeze,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandSqueeze'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'BollingerBandSqueeze': 1.0
        })
    )
