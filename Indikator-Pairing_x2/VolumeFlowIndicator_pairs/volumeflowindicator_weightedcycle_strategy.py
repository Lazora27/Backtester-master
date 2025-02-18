import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeFlowIndicator_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeFlowIndicator und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'VolumeFlowIndicator': {
                'class': VolumeFlowIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeFlowIndicator'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'VolumeFlowIndicator': 1.0,
            'WeightedCycle': 1.0
        })
    )
