import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_AverageTrueRange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und AverageTrueRange
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'AverageTrueRange': {
                'class': AverageTrueRange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AverageTrueRange1'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'AverageTrueRange': 1.0
        })
    )
