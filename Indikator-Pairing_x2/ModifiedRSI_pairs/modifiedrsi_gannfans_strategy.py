import backtrader as bt
from ..base_strategy import FlexibleStrategy

class ModifiedRSI_GannFans_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von ModifiedRSI und GannFans
    """
    
    params = (
        ('indicators', {
            'ModifiedRSI': {
                'class': ModifiedRSI,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ModifiedRSI'>
            },
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            }
        }),
        ('weights', {
            'ModifiedRSI': 1.0,
            'GannFans': 1.0
        })
    )
