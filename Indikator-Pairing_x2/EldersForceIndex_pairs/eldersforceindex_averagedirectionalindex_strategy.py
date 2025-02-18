import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_AverageDirectionalIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und AverageDirectionalIndex
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'AverageDirectionalIndex': {
                'class': AverageDirectionalIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageDirectionalIndex'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'AverageDirectionalIndex': 1.0
        })
    )
