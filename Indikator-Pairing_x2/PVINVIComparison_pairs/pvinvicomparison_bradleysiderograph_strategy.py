import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_BradleySiderograph_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und BradleySiderograph
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'BradleySiderograph': {
                'class': BradleySiderograph,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_BradleySiderograph'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'BradleySiderograph': 1.0
        })
    )
