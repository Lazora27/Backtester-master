import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticOscillator_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticOscillator und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'StochasticOscillator': {
                'class': StochasticOscillator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticOscillator'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'StochasticOscillator': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
