import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageLogRange_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageLogRange und MassIndex
    """
    
    params = (
        ('indicators', {
            'AverageLogRange': {
                'class': AverageLogRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageLogRange'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'AverageLogRange': 1.0,
            'MassIndex': 1.0
        })
    )
