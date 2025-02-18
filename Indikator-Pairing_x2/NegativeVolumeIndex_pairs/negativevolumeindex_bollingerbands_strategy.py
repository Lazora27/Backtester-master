import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und BollingerBands
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'BollingerBands': 1.0
        })
    )
