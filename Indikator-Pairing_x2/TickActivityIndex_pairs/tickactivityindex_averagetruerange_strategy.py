import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickActivityIndex_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickActivityIndex und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'TickActivityIndex': {
                'class': TickActivityIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickActivityIndex'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'TickActivityIndex': 1.0,
            'AverageTrueRange': 1.0
        })
    )
