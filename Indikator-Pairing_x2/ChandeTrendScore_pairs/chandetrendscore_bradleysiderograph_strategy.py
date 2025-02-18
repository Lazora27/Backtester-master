import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'BradleySiderograph': 1.0
        })
    )
