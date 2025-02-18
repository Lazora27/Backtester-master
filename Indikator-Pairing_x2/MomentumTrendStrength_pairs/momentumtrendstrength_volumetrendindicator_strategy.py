import backtrader as bt
from ..base_strategy import FlexibleStrategy

class MomentumTrendStrength_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von MomentumTrendStrength und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'MomentumTrendStrength': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
