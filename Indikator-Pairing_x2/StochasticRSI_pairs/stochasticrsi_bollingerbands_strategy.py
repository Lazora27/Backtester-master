import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und BollingerBands
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'BollingerBands': 1.0
        })
    )
