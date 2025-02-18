import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticTrendStrength_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticTrendStrength und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'StochasticTrendStrength': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
