import backtrader as bt
from ..base_strategy import FlexibleStrategy

class AverageTrueRange_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von AverageTrueRange und BarStrength
    """
    
    params = (
        ('indicators', {
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'AverageTrueRange': 1.0,
            'BarStrength': 1.0
        })
    )
