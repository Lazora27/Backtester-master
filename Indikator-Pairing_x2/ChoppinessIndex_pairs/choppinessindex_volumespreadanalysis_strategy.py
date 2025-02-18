import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ChoppinessIndex_VolumeSpreadAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ChoppinessIndex und VolumeSpreadAnalysis
    """
    
    params = (
        ('indicators', {
            'ChoppinessIndex': {
                'class': ChoppinessIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ChoppinessIndex'>
            },
            'VolumeSpreadAnalysis': {
                'class': VolumeSpreadAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeSpreadAnalysis'>
            }
        }),
        ('weights', {
            'ChoppinessIndex': 1.0,
            'VolumeSpreadAnalysis': 1.0
        })
    )
