import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TradeVolumeIndex_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TradeVolumeIndex und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'TradeVolumeIndex': {
                'class': TradeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TradeVolumeIndex'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'TradeVolumeIndex': 1.0,
            'WeightedCycle': 1.0
        })
    )
