import backtrader as bt
from ..base_strategy import FlexibleStrategy

class GannFans_ParabolicSAR_Strategy(FlexibleStrategy):
    """
    Kombinierte Strategie von GannFans und ParabolicSAR
    """
    
    params = (
        ('indicators', {
            'GannFans': {
                'class': GannFans,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_GannFans'>
            },
            'ParabolicSAR': {
                'class': ParabolicSAR,
                'params': <class 'backtrader.metabase.AutoInfoClass_LineRoot_LineMultiple_LineSeries_LineIterator_DataAccessor_IndicatorBase_Indicator_ParabolicSAR'>
            }
        }),
        ('weights', {
            'GannFans': 1.0,
            'ParabolicSAR': 1.0
        })
    )
