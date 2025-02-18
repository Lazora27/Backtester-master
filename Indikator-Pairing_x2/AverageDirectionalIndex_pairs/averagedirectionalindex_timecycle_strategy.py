import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_TimeCycle_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und TimeCycle
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'TimeCycle': {
                'class': TimeCycle,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TimeCycle'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'TimeCycle': 1.0
        })
    )
