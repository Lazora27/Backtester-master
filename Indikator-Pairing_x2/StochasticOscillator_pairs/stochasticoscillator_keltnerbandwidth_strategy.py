import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
