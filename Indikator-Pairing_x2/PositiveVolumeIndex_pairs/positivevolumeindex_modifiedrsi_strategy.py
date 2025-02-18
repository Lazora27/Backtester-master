import backtrader as bt
from ..base_strategy import FlexibleStrategy

class PositiveVolumeIndex_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von PositiveVolumeIndex und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'PositiveVolumeIndex': {
                'class': PositiveVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_PositiveVolumeIndex'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'PositiveVolumeIndex': 1.0,
            'ModifiedRSI': 1.0
        })
    )
