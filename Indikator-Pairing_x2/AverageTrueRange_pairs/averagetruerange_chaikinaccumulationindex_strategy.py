import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_ChaikinAccumulationIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und ChaikinAccumulationIndex
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'ChaikinAccumulationIndex': {
                'class': ChaikinAccumulationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChaikinAccumulationIndex'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'ChaikinAccumulationIndex': 1.0
        })
    )
