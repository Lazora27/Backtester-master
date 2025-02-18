import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_StochasticTrendStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und StochasticTrendStrength
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'StochasticTrendStrength': {
                'class': StochasticTrendStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticTrendStrength'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'StochasticTrendStrength': 1.0
        })
    )
