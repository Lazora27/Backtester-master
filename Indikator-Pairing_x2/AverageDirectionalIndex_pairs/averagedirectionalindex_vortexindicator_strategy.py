import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageDirectionalIndex_VortexIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageDirectionalIndex und VortexIndicator
    """
    
    params = (
        ('indicators', {
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            },
            'VortexIndicator': {
                'class': VortexIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VortexIndicator'>
            }
        }),
        ('weights', {
            'AverageDirectionalIndex': 1.0,
            'VortexIndicator': 1.0
        })
    )
