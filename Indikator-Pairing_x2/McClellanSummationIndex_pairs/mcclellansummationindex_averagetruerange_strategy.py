import backtrader as bt
from ..base_strategy import FlexibleStrategy

class McClellanSummationIndex_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von McClellanSummationIndex und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'McClellanSummationIndex': {
                'class': McClellanSummationIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_McClellanSummationIndex'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'McClellanSummationIndex': 1.0,
            'AverageTrueRange': 1.0
        })
    )
