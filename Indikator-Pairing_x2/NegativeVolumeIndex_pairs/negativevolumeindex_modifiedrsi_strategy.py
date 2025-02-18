import backtrader as bt
from ..base_strategy import FlexibleStrategy

class NegativeVolumeIndex_ModifiedRSI_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von NegativeVolumeIndex und ModifiedRSI
    """
    
    params = (
        ('indicators', {
            'NegativeVolumeIndex': {
                'class': NegativeVolumeIndex,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_NegativeVolumeIndex'>
            },
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            }
        }),
        ('weights', {
            'NegativeVolumeIndex': 1.0,
            'ModifiedRSI': 1.0
        })
    )
