import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChandeTrendScore_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChandeTrendScore und BollingerBands
    """
    
    params = (
        ('indicators', {
            'ChandeTrendScore': {
                'class': ChandeTrendScore,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChandeTrendScore'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'ChandeTrendScore': 1.0,
            'BollingerBands': 1.0
        })
    )
