import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_EhlersDecycler_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und EhlersDecycler
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'EhlersDecycler': {
                'class': EhlersDecycler,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_EhlersDecycler'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'EhlersDecycler': 1.0
        })
    )
