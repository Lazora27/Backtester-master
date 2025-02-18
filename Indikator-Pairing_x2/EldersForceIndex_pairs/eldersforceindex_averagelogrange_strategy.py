import backtrader as bt
from ..base_strategy import FlexibleStrategy

class EldersForceIndex_AverageLogRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von EldersForceIndex und AverageLogRange
    """
    
    params = (
        ('indicators', {
            'EldersForceIndex': {
                'class': EldersForceIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EldersForceIndex'>
            },
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            }
        }),
        ('weights', {
            'EldersForceIndex': 1.0,
            'AverageLogRange': 1.0
        })
    )
