import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeDelta_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeDelta und BollingerBands
    """
    
    params = (
        ('indicators', {
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'VolumeDelta': 1.0,
            'BollingerBands': 1.0
        })
    )
