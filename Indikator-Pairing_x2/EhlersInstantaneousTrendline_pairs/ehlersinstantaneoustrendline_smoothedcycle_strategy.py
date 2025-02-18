import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersInstantaneousTrendline_SmoothedCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersInstantaneousTrendline und SmoothedCycle
    """
    
    params = (
        ('indicators', {
            'EhlersInstantaneousTrendline': {
                'class': EhlersInstantaneousTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersInstantaneousTrendline'>
            },
            'SmoothedCycle': {
                'class': SmoothedCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedCycle'>
            }
        }),
        ('weights', {
            'EhlersInstantaneousTrendline': 1.0,
            'SmoothedCycle': 1.0
        })
    )
