import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PVINVIComparison_CCITurbo_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PVINVIComparison und CCITurbo
    """
    
    params = (
        ('indicators', {
            'PVINVIComparison': {
                'class': PVINVIComparison,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PVINVIComparison'>
            },
            'CCITurbo': {
                'class': CCITurbo,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_CCITurbo'>
            }
        }),
        ('weights', {
            'PVINVIComparison': 1.0,
            'CCITurbo': 1.0
        })
    )
