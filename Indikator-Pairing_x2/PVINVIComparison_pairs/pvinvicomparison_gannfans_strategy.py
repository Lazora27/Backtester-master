import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und GannFans
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'GannFans': 1.0
        })
    )
