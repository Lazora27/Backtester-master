import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'AverageTrueRange': 1.0
        })
    )
