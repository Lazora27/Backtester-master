import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_MomentumTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und MomentumTrendStrength
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'MomentumTrendStrength': {
                'class': MomentumTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_MomentumTrendStrength'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'MomentumTrendStrength': 1.0
        })
    )
