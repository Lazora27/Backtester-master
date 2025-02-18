import backtrader as bt
from ..base_strategy import FlexibleStrategy

class CumulativeTick_EhlersInstantaneousTrendline_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von CumulativeTick und EhlersInstantaneousTrendline
    """
    
    params = (
        ('indicators', {
            'CumulativeTick': {
                'class': CumulativeTick,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CumulativeTick'>
            },
            'EhlersInstantaneousTrendline': {
                'class': EhlersInstantaneousTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersInstantaneousTrendline'>
            }
        }),
        ('weights', {
            'CumulativeTick': 1.0,
            'EhlersInstantaneousTrendline': 1.0
        })
    )
