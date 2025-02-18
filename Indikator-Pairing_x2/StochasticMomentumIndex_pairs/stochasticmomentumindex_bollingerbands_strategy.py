import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticMomentumIndex_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticMomentumIndex und BollingerBands
    """
    
    params = (
        ('indicators', {
            'StochasticMomentumIndex': {
                'class': StochasticMomentumIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticMomentumIndex'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'StochasticMomentumIndex': 1.0,
            'BollingerBands': 1.0
        })
    )
