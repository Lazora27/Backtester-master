import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_VolumeDelta_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und VolumeDelta
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'VolumeDelta': {
                'class': VolumeDelta,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_VolumeDelta'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'VolumeDelta': 1.0
        })
    )
