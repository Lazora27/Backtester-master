import backtrader as bt
from ..base_strategy import FlexibleStrategy

class HighLowIndex_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von HighLowIndex und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'HighLowIndex': {
                'class': HighLowIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_HighLowIndex'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'HighLowIndex': 1.0,
            'AverageTrueRange': 1.0
        })
    )
