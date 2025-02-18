import backtrader as bt
from ..base_strategy import FlexibleStrategy

class VolumeSpreadAnalysis_AbsoluteBreadthIndex_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von VolumeSpreadAnalysis und AbsoluteBreadthIndex
    """
    
    params = (
        ('indicators', {
            'VolumeSpreadAnalysis': {
                'class': VolumeSpreadAnalysis,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeSpreadAnalysis'>
            },
            'AbsoluteBreadthIndex': {
                'class': AbsoluteBreadthIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_AbsoluteBreadthIndex'>
            }
        }),
        ('weights', {
            'VolumeSpreadAnalysis': 1.0,
            'AbsoluteBreadthIndex': 1.0
        })
    )
