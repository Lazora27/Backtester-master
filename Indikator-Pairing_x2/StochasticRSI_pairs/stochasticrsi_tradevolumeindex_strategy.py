import backtrader as bt
from ..base_strategy import FlexibleStrategy

class StochasticRSI_TradeVolumeIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von StochasticRSI und TradeVolumeIndex
    """
    
    params = (
        ('indicators', {
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            },
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            }
        }),
        ('weights', {
            'StochasticRSI': 1.0,
            'TradeVolumeIndex': 1.0
        })
    )
