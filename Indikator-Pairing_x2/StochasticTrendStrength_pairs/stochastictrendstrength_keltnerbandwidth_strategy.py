import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_KeltnerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und KeltnerBandWidth
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'KeltnerBandWidth': {
                'class': KeltnerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_KeltnerBandWidth'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'KeltnerBandWidth': 1.0
        })
    )
