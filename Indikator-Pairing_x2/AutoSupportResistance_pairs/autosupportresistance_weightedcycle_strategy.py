import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AutoSupportResistance_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AutoSupportResistance und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'AutoSupportResistance': {
                'class': AutoSupportResistance,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AutoSupportResistance'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'AutoSupportResistance': 1.0,
            'WeightedCycle': 1.0
        })
    )
