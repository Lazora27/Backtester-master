import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VWAPTimeCycleIndicator_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VWAPTimeCycleIndicator und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'VWAPTimeCycleIndicator': {
                'class': VWAPTimeCycleIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VWAPTimeCycleIndicator'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'VWAPTimeCycleIndicator': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
