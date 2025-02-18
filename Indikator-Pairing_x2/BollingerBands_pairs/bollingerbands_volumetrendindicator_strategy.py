import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_VolumeTrendIndicator_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und VolumeTrendIndicator
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'VolumeTrendIndicator': {
                'class': VolumeTrendIndicator,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeTrendIndicator'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'VolumeTrendIndicator': 1.0
        })
    )
