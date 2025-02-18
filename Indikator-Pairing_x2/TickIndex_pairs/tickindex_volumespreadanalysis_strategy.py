import backtrader as bt
from ..base_strategy import FlexibleStrategy

class TickIndex_VolumeSpreadAnalysis_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von TickIndex und VolumeSpreadAnalysis
    """
    
    params = (
        ('indicators', {
            'TickIndex': {
                'class': TickIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_TickIndex'>
            },
            'VolumeSpreadAnalysis': {
                'class': VolumeSpreadAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeSpreadAnalysis'>
            }
        }),
        ('weights', {
            'TickIndex': 1.0,
            'VolumeSpreadAnalysis': 1.0
        })
    )
