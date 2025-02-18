import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_BarStrength_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und BarStrength
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'BarStrength': {
                'class': BarStrength,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BarStrength'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'BarStrength': 1.0
        })
    )
