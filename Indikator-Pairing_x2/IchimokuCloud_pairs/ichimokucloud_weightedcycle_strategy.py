import backtrader as bt
from ..base_strategy import FlexibleStrategy

class IchimokuCloud_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von IchimokuCloud und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'IchimokuCloud': {
                'class': IchimokuCloud,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_IchimokuCloud'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'IchimokuCloud': 1.0,
            'WeightedCycle': 1.0
        })
    )
