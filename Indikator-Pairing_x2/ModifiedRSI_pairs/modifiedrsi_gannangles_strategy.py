import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_GannAngles_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und GannAngles
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'GannAngles': {
                'class': GannAngles,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannAngles1'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'GannAngles': 1.0
        })
    )
