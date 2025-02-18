import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_DeltaProfile_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und DeltaProfile
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'DeltaProfile': {
                'class': DeltaProfile,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_DeltaProfile'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'DeltaProfile': 1.0
        })
    )
