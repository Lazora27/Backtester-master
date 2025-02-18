import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
