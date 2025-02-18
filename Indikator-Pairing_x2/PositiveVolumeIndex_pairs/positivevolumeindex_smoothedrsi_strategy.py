import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_SmoothedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und SmoothedRSI
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'SmoothedRSI': {
                'class': SmoothedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_SmoothedRSI'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'SmoothedRSI': 1.0
        })
    )
