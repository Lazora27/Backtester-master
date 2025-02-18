import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und BollingerBands
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'BollingerBands': 1.0
        })
    )
