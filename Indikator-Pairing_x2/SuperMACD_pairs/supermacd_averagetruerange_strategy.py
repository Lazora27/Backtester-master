import backtrader as bt
from ..base_strategy import FlexibleStrategy

class SuperMACD_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von SuperMACD und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'SuperMACD': {
                'class': SuperMACD,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SuperMACD'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'SuperMACD': 1.0,
            'AverageTrueRange': 1.0
        })
    )
