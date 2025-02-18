import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_BidAskVolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und BidAskVolumeDelta
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'BidAskVolumeDelta': {
                'class': BidAskVolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BidAskVolumeDelta'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'BidAskVolumeDelta': 1.0
        })
    )
