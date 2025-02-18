import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NormalizedAverageTrueRange_MassIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NormalizedAverageTrueRange und MassIndex
    """
    
    params = (
        ('indicators', {
            'NormalizedAverageTrueRange': {
                'class': NormalizedAverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NormalizedAverageTrueRange'>
            },
            'MassIndex': {
                'class': MassIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MassIndex'>
            }
        }),
        ('weights', {
            'NormalizedAverageTrueRange': 1.0,
            'MassIndex': 1.0
        })
    )
