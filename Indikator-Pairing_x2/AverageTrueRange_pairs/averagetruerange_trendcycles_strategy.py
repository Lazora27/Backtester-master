import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_TrendCycles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und TrendCycles
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'TrendCycles': {
                'class': TrendCycles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TrendCycles'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'TrendCycles': 1.0
        })
    )
