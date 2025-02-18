import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_ParabolicTimePrice_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und ParabolicTimePrice
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'ParabolicTimePrice': {
                'class': ParabolicTimePrice,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicTimePrice'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'ParabolicTimePrice': 1.0
        })
    )
