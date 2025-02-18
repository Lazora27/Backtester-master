import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VortexIndicator_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VortexIndicator und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'VortexIndicator': 1.0,
            'WeightedCycle': 1.0
        })
    )
