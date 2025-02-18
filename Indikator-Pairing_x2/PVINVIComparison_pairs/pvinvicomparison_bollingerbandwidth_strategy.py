import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_BollingerBandWidth_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und BollingerBandWidth
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'BollingerBandWidth': {
                'class': BollingerBandWidth,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBandWidth'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'BollingerBandWidth': 1.0
        })
    )
