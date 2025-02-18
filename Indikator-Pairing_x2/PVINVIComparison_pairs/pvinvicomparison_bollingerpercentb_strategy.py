import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_BollingerPercentB_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und BollingerPercentB
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'BollingerPercentB': {
                'class': BollingerPercentB,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BollingerPercentB'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'BollingerPercentB': 1.0
        })
    )
