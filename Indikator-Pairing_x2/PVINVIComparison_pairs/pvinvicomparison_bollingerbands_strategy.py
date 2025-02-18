import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_BollingerBands_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und BollingerBands
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'BollingerBands': {
                'class': BollingerBands,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerBands1'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'BollingerBands': 1.0
        })
    )
