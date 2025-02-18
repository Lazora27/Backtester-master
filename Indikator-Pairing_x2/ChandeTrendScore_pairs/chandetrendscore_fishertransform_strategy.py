import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_FisherTransform_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und FisherTransform
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'FisherTransform': {
                'class': FisherTransform,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_FisherTransform'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'FisherTransform': 1.0
        })
    )
