import backtrader as bt
from ..base_strategy import FlexibleStrategy

class RateOfChange_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von RateOfChange und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'RateOfChange': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
