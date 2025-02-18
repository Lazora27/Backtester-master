import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersInstantaneousTrendline_WeightedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersInstantaneousTrendline und WeightedCycle
    """
    
    params = (
        ('indicators', {
            'EhlersInstantaneousTrendline': {
                'class': EhlersInstantaneousTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersInstantaneousTrendline'>
            },
            'WeightedCycle': {
                'class': WeightedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_WeightedCycle'>
            }
        }),
        ('weights', {
            'EhlersInstantaneousTrendline': 1.0,
            'WeightedCycle': 1.0
        })
    )
