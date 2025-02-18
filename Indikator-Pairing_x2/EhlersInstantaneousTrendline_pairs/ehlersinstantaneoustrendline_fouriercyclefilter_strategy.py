import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EhlersInstantaneousTrendline_FourierCycleFilter_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EhlersInstantaneousTrendline und FourierCycleFilter
    """
    
    params = (
        ('indicators', {
            'EhlersInstantaneousTrendline': {
                'class': EhlersInstantaneousTrendline,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersInstantaneousTrendline'>
            },
            'FourierCycleFilter': {
                'class': FourierCycleFilter,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FourierCycleFilter'>
            }
        }),
        ('weights', {
            'EhlersInstantaneousTrendline': 1.0,
            'FourierCycleFilter': 1.0
        })
    )
