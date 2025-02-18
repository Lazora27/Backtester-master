import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_StochasticRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und StochasticRSI
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'StochasticRSI': {
                'class': StochasticRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_StochasticRSI'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'StochasticRSI': 1.0
        })
    )
