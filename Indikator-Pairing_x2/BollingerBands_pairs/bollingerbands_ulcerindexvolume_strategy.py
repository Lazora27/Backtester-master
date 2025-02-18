import backtrader as bt
from ..base_strategy import FlexibleStrategy

class BollingerBands_UlcerIndexVolume_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von BollingerBands und UlcerIndexVolume
    """
    
    params = (
        ('indicators', {
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            },
            'UlcerIndexVolume': {
                'class': UlcerIndexVolume,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_UlcerIndexVolume'>
            }
        }),
        ('weights', {
            'BollingerBands': 1.0,
            'UlcerIndexVolume': 1.0
        })
    )
