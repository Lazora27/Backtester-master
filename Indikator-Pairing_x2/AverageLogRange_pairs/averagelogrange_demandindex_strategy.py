import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_DemandIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und DemandIndex
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'DemandIndex': {
                'class': DemandIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DemandIndex'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'DemandIndex': 1.0
        })
    )
