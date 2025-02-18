import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticDivergence_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticDivergence und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'StochasticDivergence': {
                'class': StochasticDivergence,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticDivergence'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'StochasticDivergence': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
