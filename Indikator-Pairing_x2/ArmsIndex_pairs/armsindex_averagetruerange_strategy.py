import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ArmsIndex_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ArmsIndex und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'ArmsIndex': {
                'class': ArmsIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ArmsIndex'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'ArmsIndex': 1.0,
            'AverageTrueRange': 1.0
        })
    )
