import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_RateOfChange_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und RateOfChange
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'RateOfChange': {
                'class': RateOfChange,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_RateOfChange1'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'RateOfChange': 1.0
        })
    )
